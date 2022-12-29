import boto3
from botocore.exceptions import ClientError
import logging


logging.basicConfig(level = logging.INFO)# we set the level at INFO
logger = logging.getLogger()# logger variable will retrieve all the INFO message


def create_sns_topic():
    """Create an SNS Topic
    Argument: None
    :return: my_topic_arn
    """
    pass
    sns_client = boto3.client('sns')
    response = sns_client.create_topic(Name='ec2-sns-topic')
    my_topic_arn = response['TopicArn']
    return my_topic_arn

def subscribe_to_topic():
    """Send a subscription to an SNS Topic
    Argument: None
    :return: response
    """
    pass
    sns_client = boto3.client('sns')
    response = sns_client.subscribe(
    TopicArn= create_sns_topic(),
    Protocol='email',
    Endpoint='maharper113@gmail.com',
    ReturnSubscriptionArn=True)

    return response

def send_email():
    """Send an email to an SNS Topic
    Argument: None
    :return: response
    """
    sns_client = boto3.client('sns')
    response = sns_client.publish(
        TopicArn = create_sns_topic(),
        Message = f'''Good Day Sir,
         Please check bucket named mimi-bucket110 on S3 for copy of
         EC2 report csv file. 
         Thanks. Mimi.''',
        Subject ='EC2 REPORT',
        )
    return response

if __name__ == '__main__':

    create_sns_topic()
    logger.info('SNS topic has been created')

    subscribe_to_topic()
    logger.info('subscription to SNS topic sent. Please validate subscription')

    send_email()
    logger.info('Email sent. Please check your email account')
