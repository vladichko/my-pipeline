#!/usr/bin/env python3
import aws_cdk as cdk
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(account="589830458041", region="eu-west-1")
)
#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
app.synth()