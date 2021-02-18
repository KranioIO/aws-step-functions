import boto3
from datetime import datetime
import json 
import os

client = boto3.client('events')
# ejecutar este script permite enviar un evento de eventbridge con el json que está en payload_mock.json
# Source y EventBusName deben coincidir SÍ O SÍ con lo que declaras en serverless.yml
# de lo contrario no llegarán los eventos a AWS.
with open("payload_mock.json", "r") as f:
            payload_mock = json.load(f)

print(type(payload_mock["payloadApp"]))
print(json.dumps(payload_mock["payloadApp"]))

response = client.put_events(
    Entries=[
        {
            'Time': datetime.now(),
            'Source': 'kranio.event.crm',
            'Resources': [
                'string',
            ],
            'DetailType': 'Inscripcion para CRM ',
            'Detail': json.dumps(payload_mock["payloadApp"]),
            'EventBusName': 'WebinarEventBus'
        },
    ]
)
print(response)