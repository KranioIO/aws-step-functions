import json
import os
import sys
from services.crm_service import CRMService

# lambda que hace /post a /crea_cliente
def handler(message, context):
    print('[crea clientes] payload entrada para crear cliente: ', message)
    crm_service = CRMService(message)
    r = crm_service.crea_cliente(message)
    print(r)
    return r


