import boto3

def list_S3_buckets():
    '''
        This function creates a list of all S3 buckets in AWS Account and appends a serial number to each bucket
        Args: None
        Returns: None
        ''' 
    my_bucket_list = []
    s3 = boto3.resource('s3')
    response = s3.buckets.all()
    print(response)
    for bucket in s3.buckets.all():
        my_bucket_list.append(bucket.name)
    number = 0
    for bucket in my_bucket_list:# looping through bucket list
        number += 1# adding +1 to each subsequent bucket
        print(f'{number},{bucket}')

if __name__ == '__main__':

    list_S3_buckets()