import json
import os
from services.crm_service import CRMService

# lambda que hace /post a /crea_beneficio
def handler(message, context):
    try:
        print('[crea clientes] payload entrada para crear beneficio: ', message)
        crm_service = CRMService(message)
        r = crm_service.create_benefit()
        # return r
        print(r)
        return message
    except Exception as e:
        print(e)
        return e