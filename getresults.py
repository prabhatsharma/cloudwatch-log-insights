import boto3

client = boto3.client('logs')

response = client.get_query_results(
    queryId = '84a0a476-e2c1-40c0-949d-0423e4a39846'
)

print(response)
