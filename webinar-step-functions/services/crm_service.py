import requests
import json
import os

# aquí deben ir tus endpoints.  idea: la url podría ser una variable de entorno, no así los endpoint que se mantienen.
# URL= os.getenv("URL")
URL="https://znyveshd7f.execute-api.us-east-2.amazonaws.com/dev"
CREATE_CLIENT = '/create_client'
CREATE_PARTNER = '/create_partner'
CREATE_BENEFIT = '/create_benefit'

class CRMService:
    def __init__(self, payload):
        self.payload = payload

    def create_client(self):
        try:
            r = requests.post(url=URL+CREATE_CLIENT, data=json.dumps(self.payload))
            if r.status_code != 200:
                return Exception (r.text)
            return json.loads(r.text)
        except Exception as e:
            return e
            

    def create_partner(self):
        try:
            r = requests.post(url=URL+CREATE_PARTNER, data=json.dumps(self.payload))
            if r.status_code != 200:
                return Exception (r.text)
            return json.loads(r.text)
        except Exception as e:
            return e
            


    def create_benefit(self):
        try:
            r = requests.post(url=URL+CREATE_BENEFIT, data=json.dumps(self.payload))
            if r.status_code != 200:
                return Exception (r.text)
            return json.loads(r.text)
        except Exception as e:
            return e
            