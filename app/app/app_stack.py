from aws_cdk import (
    Stack,
    aws_iam,
    aws_sns,
    aws_ssm,
    aws_dynamodb,
    App, Aws, CfnOutput, Duration, RemovalPolicy, Stack
)
from constructs import Construct
import aws_cdk

import os
from os import path
from dotenv import load_dotenv
load_dotenv()

class AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # get env variables
        accountid = Stack.of(self).account
        region = Stack.of(self).region

        # creates the SNS topic
        topic = aws_sns.Topic(self, "Notification Topic",
            display_name="Certificate Expiry Topic"
        )

        # create an SSM parameter for SNS ARN
        sns_arn_param = aws_ssm.StringParameter(
            self, 
            "Output SNS Topic ARN Parameter",
            parameter_name="/cert/sns_arn",
            string_value=topic.topic_arn,
            description='sns arn'
        )

        #creates a dynamodb table
        table = aws_dynamodb.Table(
            self, 
            "Table",
            table_name="cert_tracker2",
            partition_key=aws_dynamodb.Attribute(
                name="arn", 
                type=aws_dynamodb.AttributeType.STRING
                )
        )

        # create an SSM parameter for dynamodb table
        dyndb_tble_param = aws_ssm.StringParameter(
            self, 
            "Output Dynamodb Table Name Parameter",
            parameter_name="/cert/dynamodb_table",
            string_value=table.table_name,
            description='dynamodb table name'
        )
