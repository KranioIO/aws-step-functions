def handler(message, context):
    exception_message = {"success":False,"description":"ha ocurrido una excepcion en el proceso. revisar log"}
    print(message)
    return exception_message