import json
import os
from services.crm_service import CRMService

# lambda que hace /post a /crea_beneficio
def handler(message, context):
    try:
        crm_service = CRMService(message)
        res = crm_service.create_benefit()
        return res
    except Exception as e:
        print(e)
        return e