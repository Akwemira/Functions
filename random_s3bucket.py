import boto3
import random


bucket_surfix = "mimi-bucket"


s3_client = boto3.client("s3")
'''
    Description: this function creates an s3 bucket with unique name
    Arguments: bucket surfix, rand.randrange, bucket location
    Return: unique bucket created
'''
def create_unique_bucket(bucket_surfix):
    return ''.join([bucket_surfix, str(random.randrange(100, 1000, 5))])

response = s3_client.create_bucket(Bucket=create_unique_bucket(bucket_surfix), CreateBucketConfiguration={
        'LocationConstraint':'us-west-1'
    })
print(response)