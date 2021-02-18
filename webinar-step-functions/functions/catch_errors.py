def handler(message, context):
    exception_message = {
        "success":False,
        "description": "[catch_errors] Ha ocurrido una excepcion en el proceso. revisar log",
        "message": message
     }
    return exception_message