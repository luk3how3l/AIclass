#source venv/bin/activate
#############################################
# Environment loading
#############################################
import dotenv
import os
g_dotenv_loaded = False
def getenv(variable: str) -> str:
    global g_dotenv_loaded
    if not g_dotenv_loaded:
        g_dotenv_loaded = True
        dotenv.load_dotenv()
    value = os.getenv(variable)
    return value

api_key = getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY needs to be set in .env.")


#############################
#stufff
#############################

import pandas as pd
import os
import re
import time

#############################################
# 1. Load Data and Prepare for Results
#############################################
try:
    df = pd.read_csv("rag_sample_queries_candidates.csv")
    
    # Create the new column for scores ahead of time and fill with a placeholder
    df['llm_score'] = pd.NA
    print("Successfully loaded 'rag_sample_queries_candidates.csv'.")
    print("DataFrame shape:", df.shape)

except FileNotFoundError:
    print("Error: 'rag_sample_queries_candidates.csv' not found.")
    exit()

#############################################
# 2. Initialize Model
#############################################
# Replace MockOpenAIServerModel with your actual OpenAIServerModel
from smolagents import OpenAIServerModel

#model_id="gemini-2.0-flash"
#model_id="gemini-2.0-flash-lite"
model_id="gemini-2.5-flash"
model = OpenAIServerModel(model_id=model_id,
                          api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
                          api_key=api_key,
                          )


print("Model Initialized.")

#############################################
# 3. Group by Query and Loop
#############################################
# This is the core logic: group the DataFrame by the unique query ID
grouped = df.groupby('query_id')
total_groups = len(grouped)

print(f"\nFound {total_groups} unique queries to process. Starting re-ranking loop...")

# Loop through each group. 'query_id' will be the ID (e.g., 1), 
# and 'group_df' will be a DataFrame with only the rows for that query.
for i, (query_id, group_df) in enumerate(grouped):
    
    if i > 0 and i % 10 == 0:
        print("\n" + "="*50)
        print(f"Approaching rate limit. Pausing for 61 seconds...")
        print("="*50 + "\n")
        time.sleep(31) # Pause for 61 seconds to be safe
        print(f"Pausing for 30 seconds more ...")
        print("="*50 + "\n")
        time.sleep(30)
        


    # --- 4a. Get the Dynamic Query and Documents for the current group ---
    user_query = group_df['query_text'].iloc[0] # Get the query text (it's the same for all rows in the group)
    documents_to_rank = group_df.to_dict('records') # Get all candidates for this query
    
    print(f"\n({i+1}/{total_groups}) Processing Query ID: {query_id} - '{user_query[:50]}...'")
    print(f"  - Ranking {len(documents_to_rank)} candidate documents.")

    # --- 4b. Format the Prompt for the current group ---
    instruction = f"""
You are a re-ranking assistant. Rank the following documents based on relevance to the query: "{user_query}"
Provide a relevance score for each document from 0 (not relevant) to 5 (highly relevant).
Respond ONLY with a comma-separated list of numeric scores, one for each document.

--- DOCUMENTS TO RANK ---
"""
    formatted_documents = ""
    for j, doc in enumerate(documents_to_rank):
        candidate_text = doc.get('candidate_text', 'No content available.')
        formatted_documents += f"\n--- Document {j+1} ---\n{candidate_text}\n"
    
    final_prompt = instruction + formatted_documents

    # --- 4c. Call the LLM ---
    answer = model.generate(messages=[{"role": "user", "content": final_prompt}])

    # --- 4d. Parse and Store Scores ---
    try:
        score_strings = re.findall(r'[\d\.]+', answer.content)
        scores = [float(s) for s in score_strings]

        if len(scores) == len(group_df):
            # Use the group's original index to update the main DataFrame
            group_indices = group_df.index
            df.loc[group_indices, 'llm_score'] = scores
            print(f"  - Success: Received and stored {len(scores)} scores.")
        else:
            print(f"  - Error: Model returned {len(scores)} scores, but expected {len(group_df)}. Skipping update for this group.")

    except (ValueError, TypeError):
        print(f"  - Error: Could not parse model response: '{answer.content}'. Skipping update for this group.")

#############################################
# 5. Save the Final Results
#############################################
try:
    output_filename = "llm_ranked_queries_candidates4.csv"
    
    # Fill any remaining NA values (from failed groups) with 0 before saving
    df['llm_score'].fillna(0, inplace=True)
    
    df.to_csv(output_filename, index=False)
    
    print("\n" + "="*50)
    print("Re-ranking complete!")
    print(f"Successfully saved all ranked data to '{output_filename}'")
    print("="*50)
    print("\nFinal DataFrame Head:")
    print(df.head())

except Exception as e:
    print(f"\nAn error occurred while saving the file: {e}")
