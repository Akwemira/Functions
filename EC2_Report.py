import boto3
import logging
import csv
from botocore.exceptions import ClientError
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



logging.basicConfig(level = logging.INFO)# we set the level at INFO
logger = logging.getLogger()# logger variable will retrieve all the INFO message

FILENAME = 'EC2_Report.csv'

def list_ec2_instances():
    """Create a list of existing EC2 Instances in my AWS account
    :Param: None
    :Argument: None
    :return: instance_list
    """
    instance_list = []
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    
    
    #print(response['Reservations'][0]['Instances'][0]['Tags'])
    for reservation in response['Reservations']:
     
        for instance in reservation['Instances']:
            tag = instance['Tags'][0]['Value']
            imageid = instance['ImageId']
            instanceid = instance['InstanceId']
            instancetype = instance['InstanceType']
            instance_list.append([tag,imageid,instanceid,instancetype])
    return instance_list

           


def generate_csv_file(instances):
    """Create .csv file containing EC2 instances with some attributes

    :param instances: List that holds all EC2 instances in my account
    :Argument instances: List that holds all EC2 instances in my account
    :return: True if .csv file was created, else False
    """
    #csv file header
    header = ['Server Name', 'AMI ID', 'Instance ID','Instance Type']
    try:
        with open(FILENAME, 'w', newline='') as file:
            writer =  csv.writer(file)
            writer.writerow(header)
            writer.writerows(instances)
    except FileNotFoundError as error:
        logger.error(f"file does not exist: {error}") 
        return False
    return True

def upload_to_s3bucket(file_name, bucket, object_name):
    """Upload .csv file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    try:
        s3_client = boto3.resource('s3')
        response = s3_client.meta.client.upload_file(FILENAME, 'mimi-bucket110', 'ec2-excel-list')
    except ClientError as error:
        logger.error(f'Unable to upload file to S3 because {error}')
        return False
    return True

def verify_email_identity():
    """Verify an email identity with Amazon SES
    Argument: None
    :return: True if Email identity was verified, else False
    """
    try:
        ses_client = boto3.client("ses", region_name="us-west-1")
        response = ses_client.verify_email_identity(
            EmailAddress="maharper113@gmail.com"
        )
    except ClientError as error:
        logger.error(f'email verification failed because {error}')
        return False
    return True

def send_email_plus_attachment():
    """Send email with attachment
    :param: None
    :Argument: None
    :return: True if email was sent, else False
    """
    msg = MIMEMultipart()
    msg["Subject"] = "EC2 REPORT"
    msg["From"] = "maharper113@gmail.com"
    msg["To"] = "maharper113@gmail.com"

    # Set message body
    body = MIMEText(f"""Hello Sir, 

    Writing to update you on the EC2 report.
    Find attached {FILENAME}.

    Sincerely,

    Mimi.
    """)
    msg.attach(body)


    with open(FILENAME, "rb") as attachment:
        part = MIMEApplication(attachment.read())
        part.add_header("Content-Disposition",
                        "attachment",
                        filename=FILENAME)
    msg.attach(part)
    try:
        # I convert message to string and send it using SES
        ses_client = boto3.client("ses", region_name="us-west-1")
        response = ses_client.send_raw_email(
            Source="maharper113@gmail.com",
            Destinations=["maharper113@gmail.com"],
            RawMessage={"Data": msg.as_string()}
        )
    except FileNotFoundError as error:
        logger.error(f'Email not sent because of: {error}')
        return False
    return True




if __name__ == '__main__':

    logger.info(f'Our list of servers: {list_ec2_instances()}')

    instances = list_ec2_instances()
    logger.info('List of instances has been created')

    generate_csv_file(instances)
    logger.info('Excel file has been generated')

    upload_to_s3bucket(FILENAME, 'mimi-bucket110', 'ec2-excel-list')
    logger.info('Excel file has been uploaded to S3 bucket')

    verify_email_identity()
    logger.info('Please check your email and validate the SES request to use your email address')

    send_email_plus_attachment()
    logger.info('Email was sent. Please check your inbox')