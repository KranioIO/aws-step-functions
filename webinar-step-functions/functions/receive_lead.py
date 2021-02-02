import json 
from services.parse_event import parse_event_eventbridge

# lambda que recibe evento desde eventbridge de forma exitosa
def handler(message, context):
    print('Recibiendo evento...')
    return message["detail"]

