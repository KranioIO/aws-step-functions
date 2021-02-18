import json
from services.crm_service import CRMService

# lambda que hace /post a /crea_cliente
def handler(message, context):
    try:
        crm_service = CRMService(message)
        crm_service.create_client()
        return message
    except Exception as e:
        print ("Exception: ", e)
        return e