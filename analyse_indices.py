import boto3

KB_ID = "ICRJS7XFZ5"

QUERY = """ 

you have been provided with the closing price for major stock indices . 
1)Can you generate the annualized returns for each series and summarize the results in a table format 
2)Can you generate the annualized standard deviation for each series using the daily returns and summarize the results in a table format
3) Compare the annualized returns and standard deviation of the series and provide your analysis in a table format
4) Rank the indices based on the annualized returns for the current year and provide your analysis in a table format
5) Based on the ranking of the indices, allocate a weight of 0.3 to the top 2 indices and 0.2 to the next 2 indices. Based on this what will be the annualized return, annualized volatility
6) What is the best time to invest in these indices based on the ranking and the annualized returns and annualized volatility
7) Compare it to a momentum strategy and provide your analysis in a table format
"""

REGION = "us-east-1"
MODEL = "anthropic.claude-3-haiku-20240307-v1:0"
NUM_RESULTS = 1

# Setup bedrock
bedrock_agent_runtime = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name=REGION,
)


docs_only_response = bedrock_agent_runtime.retrieve(
    knowledgeBaseId=KB_ID,
    retrievalQuery={"text": QUERY},
    retrievalConfiguration={
        "vectorSearchConfiguration": {"numberOfResults": NUM_RESULTS}
    },
)

text_response = bedrock_agent_runtime.retrieve_and_generate(
    input={"text": QUERY},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": KB_ID,
            "modelArn": MODEL,
        },
    },
)

print(text_response['output']['text'])

