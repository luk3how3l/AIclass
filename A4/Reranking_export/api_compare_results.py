
################################
#pull dataframe
################################
import pandas as pd
try:
    #lite-quick is 3
    #just lite is 4 
    output_filename = "llm_ranked_queries_candidates4.csv"
    
    df = pd.read_csv(output_filename)
    df_head = df.head()
    #print(df.head().iloc[0:4,2:4])

    print("\n Post_Creation DataFrame columns selected for", output_filename[:-3])
    print(df.head()) # Print the first 5 rows of the selection

except FileNotFoundError:
    print("Error: 'rag_sample_queries_candidates.csv' not found.")
    exit()

###########
#error checking
print("Checking for missing values (NaNs):")
print(df.isnull().sum())

#############################################
# Evaluate Rankings
#############################################

from sklearn.metrics import ndcg_score
import numpy as np

def precision_at_k(y_true, k=3):
    return np.sum(y_true[:k]) / k

def recall_at_k(y_true, k=3):
    return np.sum(y_true[:k]) / np.sum(y_true)

for qid, group in df.groupby("query_id"):
    y_true = group.sort_values("baseline_rank")["gold_label"].to_numpy()
    y_pred = group.sort_values("baseline_rank")["baseline_score"].to_numpy()
    baseline_ndcg = ndcg_score([y_true], [y_pred])
    
    y_pred_llm = group.sort_values("llm_score", ascending=False)["llm_score"].to_numpy()
    ndcg_llm = ndcg_score([y_true], [y_pred_llm])
    
    print(f"Query {qid}: baseline nDCG={baseline_ndcg:.3f}, LLM nDCG={ndcg_llm:.3f}")



