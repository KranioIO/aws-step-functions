""" escribe en la db """
import os
from libs.api_responses import response_success, response_server_error
from database.db import connect, return_tuple, create_record
from database.script import INSERT_BENEFIT
import json
def handler(message, context):
    try:
        msg = json.loads(message["body"])
        data = return_tuple(
            msg["rut"],
            msg["wantsBenefit"]
            )

        conn = connect()
        res = create_record(conn, INSERT_BENEFIT, data)
        return response_success(res["success"], res["message"]) 
    except Exception as e:
        print("Exception: ", e)
