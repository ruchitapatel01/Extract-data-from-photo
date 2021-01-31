import json
import boto3
import base64

s3 = boto3.client("s3")

def lambda_handler(event, context):
    
    print(event)
    bucket = "upload-photo"
    key = event["key"]
    
    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        json_data = data["Body"].read().decode("utf-8")
        
        return json_data
        
        # return {
        #     "response_code" : 200,
        #     "data" : str(data)}
    except Exception as e:
        print(e)
