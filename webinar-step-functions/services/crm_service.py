import requests
import json
import os

# aquí deben ir tus endpoints.  idea: la url podría ser una variable de entorno, no así los endpoint que se mantienen.
URL = 'https://8p97jqny87b.execute-api.us-east-2.amazonaws.com/dev'
CREA_CLIENTE = '/crea_cliente'
CREA_SOCIO = '/crea_socio'
CREA_BENEFICIO = '/crea_beneficio'

class CRMService:
    def __init__(self, payload):
        self.payload = payload

    def crea_cliente(self, payload):
        r = requests.post(url=URL+CREA_CLIENTE, data=payload)
        if r.status_code != 200:
            return Exception (r.text)
        return json.loads(r.text)
    
    def crea_socio(self, payload):
        r = requests.post(url=URL+CREA_SOCIO, data=payload)
        return json.loads(r.text)
    
    def crea_beneficio(self, payload):
        r = requests.post(url=URL+CREA_BENEFICIO, data=payload)
        return json.loads(r.text)        
