import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

# Set dynamodb table name variable from env
ddbTableName = os.environ['TABLE_NAME']
table = dynamodb.Table(ddbTableName)

def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={
            'id': 'ViewsCountId'
        },
        #instead of posting the views value every time, just update
        #current entry by one
        UpdateExpression='SET viewsCount = viewsCount + :value',
        ExpressionAttributeValues={
            ':value': Decimal(1)
        },
        ReturnValues="UPDATED_NEW"
    )

    # Format into variable
    responseBody = ddbResponse["Attributes"]["viewsCount"]

    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        #add cors headers
        'headers': {
            'Access-Control-Allow-Origin': os.environ['CORS_URL']
        },
        "body": responseBody
    }

    # Return api response object
    return apiResponse