import json
import os
from services.crm_service import CRMService

# lambda que hace /post a /crea_beneficio
def handler(message, context):
    print('[crea clientes] payload entrada para crear beneficio: ', message)
    crm_service = CRMService(message)
    r = crm_service.crea_beneficio(message)
    return r
