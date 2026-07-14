import json
import boto3
import os

s3 = boto3.client('s3')

TAG_KEY = os.environ.get('TAG_KEY', 'Owner')
TAG_VALUE = os.environ.get('TAG_VALUE', 'devops student')

def lambda_handler(event, context):
    print('Received event:', json.dumps(event))
    
    try:
        bucket_name = event['detail']['requestParameters']['bucketName']
    except Exception as e:
        print('Could not extract bucket name:', str(e))
        return
    
    try:
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={'TagSet': [{'Key': TAG_KEY, 'Value': TAG_VALUE}]}
        )
        print(f'Successfully tagged bucket: {bucket_name}')
    except Exception as e:
        print(f'Error tagging bucket {bucket_name}: {str(e)}')
        raise
