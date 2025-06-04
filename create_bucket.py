import boto3

client = boto3.client ('s3')

response = client.create_bucket(
    Bucket='gracious-practice-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

print(response)

response = client.put_object(
    Body='mug.jpg',
    Bucket='gracious-practice-bucket',
    Key='mug.jpg',
    ContentType = "image/jpg"
)

print(response)

