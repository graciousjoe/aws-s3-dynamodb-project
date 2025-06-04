import boto3
from uuid import uuid4

dynamodb = boto3.resource ('dynamodb', region_name = 'eu-west-1')

table = dynamodb.Table('students')

response = table.get_item(
    Key={
        'pk': {
            'S': 'student',
        },
        'sk': {
            'S': '29cbfe33-79b9-45cf-bda5-76616a24f303',
        },
    },
    TableName='students',
)

print(response)