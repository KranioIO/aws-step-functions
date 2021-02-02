import json
import os
import sys
from services.crm_service import CRMService

# lambda que hace /post a /crea_socio
def handler(message, context):
    try:
        print(context)
        print('[crea clientes] payload entrada para crear socio: ', message)
        crm_service = CRMService(message)
        r = crm_service.create_partner()
        # return r
        print(r)
        return {
            "success": True

        }
        # return message
    except Exception as e:
        print(e)
        return e


