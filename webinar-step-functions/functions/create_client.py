import json
from services.crm_service import CRMService

# lambda que hace /post a /crea_cliente
def handler(message, context):
    try:

        print("Message: ", message)
        print(type(message))
        print('[crea clientes] payload entrada para crear cliente: ', message)
        crm_service = CRMService(message)
        r = crm_service.create_client(message)
        print(r)
        return message
    except Exception as e:
        print ("Exception: ", e)
        return e


# msg = {
#     "name": "sanddro",
# 	"lastname": "de america",
#     "rut": "4758433-0",
#     "phone": 987566787,
#     "mail": "leoace@micorreo.com",
#     "store": "la florida",
#     "wantsBenefit": True,
#     "origin": "app"
#   }
# res = handler(msg, None)   
# print(res)