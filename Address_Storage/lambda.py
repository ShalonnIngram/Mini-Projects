import boto3
import json 

glue_client = boto3.client('glue')

def lambda_handler(event, context):
    glue_client.start_job_run(JobName = 'marketingetlmay')
    return 'Your Glue Job has started'
