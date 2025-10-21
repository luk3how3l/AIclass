
################################
#pull dataframe
################################
import pandas as pd

#lite-quick is 3
#just lite is 4 
output_filename = "llm_ranked_queries_candidates4.csv"

try:
    df = pd.read_csv(output_filename)
    df['llm_rank'] = pd.NA
    df_head = df.head()
    
    print("\n Post_Creation DataFrame columns selected for", output_filename[:-4])
    print(df.head()) # Print the first 5 rows of the selection

except FileNotFoundError:
    print("Error: 'rag_sample_queries_candidates.csv' not found.")
    exit()

#############################################
#error checking
#############################################
'''
print("Checking for missing values (NaNs):")
print(df.isnull().sum())
'''

#############################################
# Evaluate Rankings
#############################################

from sklearn.metrics import ndcg_score
import numpy as np

def precision_at_k(y_true, k=3):
    topk = labels[:k]
    return np.sum(topk) / len(topk)

def recall_at_k(y_true, k=3):
    """Recall = retrieved relevant / total relevant"""
    total_relevant = np.sum(labels)
    if total_relevant == 0:
        return np.nan  # undefined
    topk = labels[:k]
    return np.sum(topk) / total_relevant

def ndcg_at_k(labels, k):
    """Compute nDCG@k with binary relevance (0/1)."""
    labels = np.array(labels)
    k = min(k, len(labels))
    gains = (2 ** labels[:k] - 1)
    discounts = 1 / np.log2(np.arange(2, k + 2))
    dcg = np.sum(gains * discounts)

    # Ideal DCG: sorted by true relevance
    ideal = np.sort(labels)[::-1]
    ideal_gains = (2 ** ideal[:k] - 1)
    idcg = np.sum(ideal_gains * discounts)
    return 0.0 if idcg == 0 else dcg / idcg

def evalute_ranking(data,score_col,k=3):
    metric =[]

    # SORt by score descending
    rank_data = data.sort_values(["query_id",score_col], ascending=[True,False]).copy()

    for qid, group in rank_data.groupby("query_id"):
        
        labels = group["gold_label"].tolist()
        p = precision_at_k(labels, k)
        r = recall_at_k(labels, k)
        n = ndcg_at_k(labels, K)
        #get ture wo sorting
        y_true = group["gold_label"].to_numpy().reshape(1, -1)
        y_score = group[score_col].to_numpy().reshape(1, -1)
        


        metric.append({

            "query_id": qid,
            f"precision@{K}":p,
            f"recall@{K}": r,
            f"nDCG@{K}": n 
            })
    return pd.DataFrame(metric)

#############################################
# Evaluate Rankings
#############################################
print("\n--- Ranking Evaluation ---")
K = 3
baseline_metrics = evalute_ranking(df, "baseline_score")
llm_metrics = evalute_ranking(df, "llm_score")

print("\nBaseline Metrics:")
print(baseline_metrics.head())

print("\nLLM Metrics:")
print(llm_metrics.head())

#average scores metric
print("\nAverage baseline nDCG:", baseline_metrics[f"nDCG@{K}"].mean())
print("Average LLM nDCG:", llm_metrics[f"nDCG@{K}"].mean())


#############################################
# Insert into results.csv / with llm_rank included
#############################################
try:
    
    df["baseline_rank"] = df.groupby("query_id")["baseline_score"] \
        .rank(ascending=False, method="first")

    df["llm_rank"] = df.groupby("query_id")["llm_score"] \
        .rank(ascending=False, method="first")


    # Fill any remaining NA values (from failed groups) with 0 before saving
    df['llm_rank'].fillna(0, inplace=True)
    
    output_filename = "rankings.csv"
    df.to_csv(output_filename, index=False)
    
    print("\n" + "="*50)
    print("Re-ranking complete!")
    print(f"Successfully saved all ranked data to '{output_filename}'")
    print("="*50)
    print("\nFinal DataFrame Head:")
    print(df.head())

except Exception as e:
    print(f"\nAn error occurred while saving the file: {e}")