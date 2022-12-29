import boto3



def create_ec2_instance():
    '''
    This function creates 4 t2.micro EC2 Instances in US-WEST-1 region
    Args: None
    Returns: None

        ''' 

    client = boto3.client('ec2', region_name='us-west-1')
    response = client.run_instances(
        BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {

                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp2'
            },
        },
    ],
    ImageId='ami-00d8a762cb0c50254',
    InstanceType='t2.micro',
    MaxCount=4,
    MinCount=4,
    Monitoring={
        'Enabled': False
    },
    
)
    listing = []
    #print(response['Instances'][0]['InstanceId'])
    for instances in response['Instances']:
        print(instances['InstanceId'])
        







if __name__ == '__main__':
    create_ec2_instance()