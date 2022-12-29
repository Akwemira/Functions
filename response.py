response = {
    'ResponseMetadata': {
        'RequestId': 'H280C36V5ZHMZBQX', 
        'HostId': 'NruZTeJIZo6plKnEaqXCVwlJd6D7/eqioUdp/vtXJoxd+hp7ktxqpthrwbZeSKKav5yoH1zzTO0=', 
        'HTTPStatusCode': 200, 
        'HTTPHeaders': {
            'x-amz-id-2': 'NruZTeJIZo6plKnEaqXCVwlJd6D7/eqioUdp/vtXJoxd+hp7ktxqpthrwbZeSKKav5yoH1zzTO0=', 
            'x-amz-request-id': 'H280C36V5ZHMZBQX', 
            'date': 'Wed, 14 Dec 2022 14:02:19 GMT', 
            'location': 'http://mimi-bucket315.s3.amazonaws.com/', 
            'server': 'AmazonS3', 
            'content-length': '0'},
        'RetryAttempts': 0
    }, 
 'Location': 'http://mimi-bucket315.s3.amazonaws.com/'}

print(response['Location'].split(".")[0].split("/")[2])