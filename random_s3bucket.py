'''
random_s3bucket.py
'''
import boto3
import random


bucket_prefix = "mimi-bucket"


s3_client = boto3.client("s3")

def create_unique_bucket(bucket_prefix):
    '''
    Description: this function creates an s3 bucket with unique name
    Arguments: bucket_prefix,
    Return: unique bucket created
    '''
    return ''.join([bucket_prefix, str(random.randrange(100, 1000, 5))])

response = s3_client.create_bucket(Bucket=create_unique_bucket(bucket_prefix), CreateBucketConfiguration={
        'LocationConstraint':'us-west-1'
    })
print(response)
print(response['ResponseMetadata']['HTTPHeaders']['location'].split('.')[0].split('/')[2])
#print(create_unique_bucket(bucket_surfix))

if __name__ == '__main__':

    create_unique_bucket(bucket_prefix)