#!/usr/bin/env python3
import os
import settings

import aws_cdk as cdk

from app.app_stack import AppStack
from app.lambda_stack import LambdaStack
from aws_cdk import App, Tags, Environment

env_main = cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),    
    region='us-east-1'
    )

app = cdk.App()
app_stack= AppStack(
    app, 
    "AppStack",
    env=env_main
    )

lambda_stack= LambdaStack(
    app, 
    "LambdaStack",
    env=env_main
    )

Tags.of(app_stack).add("ApplicationGroup", "MultiAccount2021")
Tags.of(lambda_stack).add("ApplicationGroup", "MultiAccount2021")

app.synth()
