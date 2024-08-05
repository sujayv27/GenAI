import boto3

KB_ID = "ICRJS7XFZ5"

QUERY = """ Based on the data provided to you . Can you answer the below queries 
1) Can you provide some statistic analysis of the data 
2) Is there any lagged correlation between prices of different time series
3)Can you find the average returns of each series
4)Can you backtest a momentum strategy and tell me how it performs, for example, every 5 trading days, if the historical 5 days average return is bigger than historical 20 days average return, we long 1 unit of the stock, otherwise we don't do anything.
5) Can you try a few other sets of lookback periods for moving averages and compare their performances?
6) Can you provide the data in a table format
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
