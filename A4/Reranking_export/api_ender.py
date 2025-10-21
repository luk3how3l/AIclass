#!/usr/bin/env python3
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


#############################################
# Query stealer
#############################################
import pandas as pd
try:
    df = pd.read_csv("rag_sample_queries_candidates.csv")
    df.head()
    print(df.head().iloc[0:4,2:4])

    #grab which query goes to which to ask the right one in groups of five. loop 
    query_text_df = df.iloc[:,1:2]
    list_of_dict = selected_df.to_dict(orient='records')
    #should delete duplicate since same 1 goes to same query
    print(query_text_df.head())

    #grab just the all rows but just columns 2:4 and put it into an dictionary and print it
    #do something
    selected_df = df.iloc[:, 2:4]
    dict_of_lists = selected_df.to_dict(orient='list')
    list_of_dicts = selected_df.to_dict(orient='records')

    print(list_of_dicts[:5])
    print("\nOriginal DataFrame columns selected:")
    print(selected_df.head()) # Print the first 5 rows of the selection

except FileNotFoundError:
    print("Error: 'rag_sample_queries_candidates.csv' not found.")
    exit()

#############################################
#  Content question
#############################################
content1= "Can you rank the response I give me you this question: What is reinforcement learning? Rank based on how relevant to this question. scale to 0 (low) to 5 (high), respond only with an number"
user_query = "What is reinforcement learning?"
#[:] all of d
rank_content= list_of_dicts[:]

#formattt
instruction = f"""
You are a re-ranking assistant. Your task is to rank the following documents based on how relevant they are to the user's query.
The query is: "{user_query}"

Please provide a relevance score for each document on a scale from 0 (not relevant) to 5 (highly relevant).
Respond ONLY with a comma-separated list of the numeric scores, one for each document.
Example Response: 5.0, 1.5, 4.0, 2.0, 3.5

--- DOCUMENTS TO RANK ---
"""
formatted_documents = ""
for i, doc in enumerate(rank_content):
    # CSV has a 'candidate_text' column
    candidate_text = doc.get('candidate_text', 'No content available.')
    formatted_documents += f"\n--- Document {i+1} ---\n{candidate_text}\n"

# This is the final prompt
final_prompt = instruction + formatted_documents




#############################################
# Model connection
#############################################
from smolagents import OpenAIServerModel

#model_id="gemini-2.0-flash"
#model_id="gemini-2.0-flash-lite"
model_id="gemini-2.5-flash-lite"
model = OpenAIServerModel(model_id=model_id,
                          api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
                          api_key=api_key,
                          )

answer = model.generate(messages=[{
    "role": "user", 
    "content": final_prompt
}])

print(f"Model returned answer: {answer.content}")

"""
Parse the numeric response into a float `llm_score`.  
Store all results in a new column in your DataFrame.

"""
#############################################
# 4. Parse the Response and Update DataFrame
#############################################
import re

llm_response = answer.content
scores = []

#parse the good stuff
score_strings = re.findall(r'[\d\.]+', llm_response)
scores = [float(s) for s in score_strings]


print(scores)

if len(scores) == len(rank_content):
        # Assign the list of scores to a new column for the first N rows
        # .loc is used to ensure we are modifying the original DataFrame
        df.loc[:len(scores)-1, 'llm_score'] = scores
        
        print("\nSuccessfully parsed scores and updated DataFrame.")
        # Display the head of the DataFrame with the new column
        print(df[['candidate_id', 'candidate_text', 'llm_score']].head())
else:
    print(f"\nError: The model returned {len(scores)} scores, but we sent {len(rank_content)} documents.")

#############################################
# Save the results into new file
#############################################
#1 was head demo only 5.
#2 now all 103 queries ranking
try:
    output_filename = "llm_ranked_queries_candidates2.csv"
    
    # Use the .to_csv() method to save the DataFrame
    # index=False prevents pandas from writing the DataFrame index as a column
    df.to_csv(output_filename, index=False)
    
    print("\n" + "="*50)
    print(f"Successfully saved the ranked data to '{output_filename}'")
    print("="*50)

except Exception as e:
    print(f"\nAn error occurred while saving the file: {e}")

