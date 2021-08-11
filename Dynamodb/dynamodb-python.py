import os
import sys
import datetime
import time

import boto3

db = boto3.resource( "dynamodb",
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name="us-east-1")

table = db.Table("employees")
table.put_item(
    Item={
        'emp_id': "2",
        'name': "Joe",
        'Age': "32"
    }
)
response = table.get_item(
    Key={
        'emp_id': "2",
    }
)
print(response["Item"])