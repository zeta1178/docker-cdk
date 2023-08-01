import json
import boto3 
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
import os

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cert_tracker')
    #
    response = table.scan(FilterExpression = Attr('certificate_daysleft').lt(15))
    data = response['Items']
    if len(data) == 0  :
        print('No certificates are due to expire within the next 2 weeks.')
    else:
        for d in data:
            #
            sns = boto3.client('sns')
            # body='''Test'''
            mess={"Default": "Message"}
            mess_bdy  = f"This certifate will expire in 14 days or less, \n\n {d}\n\n address immediately."
            # sns_arn='arn:aws:sns:us-east-1:992690408789:cert_exp'
            sns_arn=os.getenv('SNS_TOPIC_ARN')
            #
            sns_response= sns.publish(
                TargetArn=sns_arn,
                Message=json.dumps(
                    {
                        "default": json.dumps(mess),
                        "email": mess_bdy,
                    }
                    ),
                Subject="Certificate Expiration Notice",
                MessageStructure='json'
                )