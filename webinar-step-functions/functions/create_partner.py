import json
import os
import sys
from services.crm_service import CRMService

# lambda que hace /post a /crea_socio
def handler(message, context):
    try:
        crm_service = CRMService(message)
        crm_service.create_partner()
        return message
    except Exception as e:
        print(e)
        return e
