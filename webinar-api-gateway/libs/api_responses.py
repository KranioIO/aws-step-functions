import json

def response_success(message, description):
    body = {
        "statusCode": 200,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(body)
    }

def response_created(message, description):
    body = {
        "statusCode": 201,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 201,
        "headers": {},
        "body": json.dumps(body)
    }

def response_accepted(message, description):
    body = {
        "statusCode": 202,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 202,
        "headers": {},
        "body": json.dumps(body)
    }

def response_bad_request(message, description):
    body = {
        "statusCode": 400,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 400,
        "headers": {},
        "body": json.dumps(body)
    }

def response_not_found(message, description):
    body = {
        "statusCode": 404,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 404,
        "headers": {},
        "body": json.dumps(body)
    }

def response_server_error(message, description):
    body = {
        "statusCode": 500,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 500,
        "headers": {},
        "body": json.dumps(body)
    }

def response_conflict(message, description):
    body = {
        "statusCode": 409,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 409,
        "headers": {},
        "body": json.dumps(body)
    }
