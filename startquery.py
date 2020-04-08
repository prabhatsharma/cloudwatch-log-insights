import boto3
import datetime as dt

client = boto3.client('logs')

response = client.start_query(
    logGroupName='/aws/eks/basic3/cluster',
    # logGroupNames=[
    #     'string',
    # ],
    # startTime=1586304000,
    startTime = int(dt.datetime(2020,4,7,0,0,0).timestamp()),
    endTime   = int(dt.datetime(2020,4,7,0,0,1).timestamp()),
    queryString='fields @timestamp, @message | sort @timestamp desc',
    limit=10000
)

print(response)
