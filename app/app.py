#!/usr/bin/env python3
import os

import aws_cdk as cdk

from app.app_stack import AppStack
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

app.synth()
