# from aws_cdk import aws_lambda_python_alpha as lambda_alpha

from aws_cdk import (
    Aws,
    Duration,
    Stack,
    CfnOutput,
    aws_ssm,
    aws_lambda,
    aws_iam as iam,
)
from constructs import Construct

class LambdaStack(Stack):

    # def __init__(self, scope: Construct, construct_id: str, props, referenced_key: kms.IKey ,**kwargs) -> None:
    def __init__(self, scope: Construct, construct_id: str, props, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # lookup sns_arn
        # sns_arn_param = aws_ssm.StringParameter.value_for_string_parameter(
        sns_arn_param = aws_ssm.StringParameter.value_from_lookup(
            self, "/cert/sns_arn")
        
        # permissions for SNS for Lambda Function
        perm_statement_sns = iam.PolicyStatement()
        perm_statement_sns.add_actions(
                "sns:*",
            )
        perm_statement_sns.add_resources("*") #This adds to the Lambda function a policy granting access        

        # permissions for SSM for Lambda Function
        perm_statement_ssm = iam.PolicyStatement()
        perm_statement_ssm.add_actions(
                "ssm:DescribeParameters",
                "ssm:GetParameter",
                "ssm:GetParameterHistory",
                "ssm:GetParameters"
            )
        # ssm_param         =f"arn:aws:ssm:{Aws.REGION}:{Aws.ACCOUNT_ID}:parameter/cert/*"
        ssm_param=sns_arn_param
        perm_statement_ssm.add_resources(ssm_param)

        # permissions for VPC for Lambda Function
        perm_statement_vpc = iam.PolicyStatement()
        perm_statement_vpc.add_actions(
            "ec2:*",
        )
        perm_statement_vpc.add_resources("*") #This adds to the Lambda function a policy granting access

        # modify with existing VPC ID
        # referenced_vpc=ec2.Vpc.from_lookup(self, "VPC",vpc_id = 'vpc-09fdcfa8364dbd334' )

        #modify with existing Private Subnet group or Subnet IDs
        # referenced_subnet=ec2.SubnetSelection(subnets = ['subnet-0516d62225de0912f'])
        # referenced_subnet=ec2.SubnetSelection(subnet_group_name="Private")

        #creates the lambda function
        lambda_Fn = aws_lambda.PythonFunction(
            self, "excel lambda",
            entry="./lambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            index="lambda_function.py",
            handler="lambda_handler",
            memory_size=512,
            timeout=Duration.seconds(60),
            # vpc=referenced_vpc,
            # vpc_subnets=referenced_subnet, 
            environment={
              "SNS_TOPIC_ARN" : sns_arn_param ,
            },
        )

        #Adds policies to the role
        lambda_Fn.add_to_role_policy(perm_statement_ssm) #This adds the policy to the role.
        lambda_Fn.add_to_role_policy(perm_statement_vpc) #This adds the policy to the role.
        lambda_Fn.add_to_role_policy(perm_statement_sns) #This adds the policy to the role.
