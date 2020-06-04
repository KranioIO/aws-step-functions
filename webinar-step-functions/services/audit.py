import boto3
from datetime import datetime

dynamo_client = boto3.client('dynamodb')

def write_stepfunction_data(message):
    rut = message["detail"]["rut"]
    event_id = message["id"]
    response = dynamo_client.put_item(
        TableName='TablaAuditoriaCRM',
        Item=
            {
                'rut':{
                    'S':rut
                },
                'event_id':{
                    'S':event_id
                }                
            }
    )
    print('Se ha registrado el ID del evento: %s con el rut: %s' % (event_id, rut))


