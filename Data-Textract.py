import boto3
import json
import sys
from pprint import pprint

textract = boto3.client(
    service_name='textract',
    region_name='us-east-1')
    
s3 = boto3.resource('s3')
s3_put = boto3.client('s3')


def lambda_handler(event, context):
    # TODO implement
    
    data = ""
    object_key = event['Records'][0]['s3']['object']['key']
    
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': 'upload-photo',
                'Name': event['Records'][0]['s3']['object']['key']
            }
        }
    )
    
    print('')
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            # print(item["Text"])
            data = data + item["Text"] + '\n'
            print(data)
    print('')
    
    
    # data = "Hello From lambda console."
    filename = object_key.rsplit('.', 1)[0] + '.txt'
    # print(filename)
    
    uploadByteStream = bytes(data.encode('UTF-8'))
    
    s3_put.put_object(Bucket="upload-photo", Key=filename, Body=uploadByteStream)
    
    print("Put Done.")
    
    
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from lambda!")
    }
