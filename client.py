import os
import json
import http.client, urllib.parse

import boto3
import requests


BASE_URL = 'api.marketaux.com'


def get_entity_data(token, limit=None):
    symbol = 'TSLA'
    if limit is None:
        limit = 1

    params = urllib.parse.urlencode({
        'api_token': api_token,
        'symbols': symbol,
        'limit': limit,
        })
    
    endpoint = '/v1/news/all'
    conn = http.client.HTTPSConnection(BASE_URL)
    conn.request('GET', '{}?{}'.format(endpoint,params))
    response = conn.getresponse()
    data = response.read()

    return data


def send_alert():
    api_token = os.environ['TOKEN']
    topic_arn = os.environ['TOPIC_ARN']
    data = json.loads(get_entity_data(api_token))
    title = data['data'][0]['title']
    url = data['data'][0]['url']

    client = boto3.client('sns')
    message = json.dumps({'title': title, 'url': url})
    response = client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject='stock update',
    )
    return response


message_status = send_alert()
print(message_status)