import boto3

KB_ID = "ICRJS7XFZ5"
QUERY = "How do we define the trend signal?. Can you provide a mathematical formula for it \
and write the python code for it and can you run the code by reading the data as provided in SPX.csv and print the result time series in a csv "




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
