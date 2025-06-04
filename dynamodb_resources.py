import boto3
from uuid import uuid4

dynamodb = boto3.resource ('dynamodb', region_name = 'eu-west-1')

table = dynamodb.Table('students')

user1 = {
    "pk": "student",
    "sk": str(uuid4()),
    "first_name": "Gracious",
    "last_name": "Joseph",
    "ID": "001",
    "Email": "graciousjoseph@gamil.com"
}

user2 = {
    "pk": "student",
    "sk": str(uuid4()),
    "first_name": "Kelvin",
    "last_name": "Ayisi",
    "ID": "002",
    "Email": "kelvinayisi@gamil.com"
}

response = table.put_item(
    Item = user1
)
response = table.put_item(
    Item = user2
)

print(response)

