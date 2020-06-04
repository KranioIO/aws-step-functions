import boto3
from datetime import datetime
import json 
import os
from services.parse_evento import parse_event_eventbridge

# lambda que recibe evento desde eventbridge de forma exitosa
def handler(message, context):
    print('recibiendo evento...')
    inscripcion_recibida = parse_event_eventbridge(message)
    return inscripcion_recibida

