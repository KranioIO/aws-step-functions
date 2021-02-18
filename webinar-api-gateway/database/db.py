import pymysql
import os
import sys
# from script import CREATE_TABLE_CLIENTS

# dejar como variable de entorno y si hay tiempo usar ssm
DB_USER = os.getenv('db_user')
DB_PASS = os.getenv('db_pass')
DB_NAME = os.getenv('db_name')
DB_PORT = os.getenv('db_port')
DB_HOST = os.getenv('db_host')

def connect():
    # funcion para conectarse a la db
    try:
        conn = pymysql.connect(
            host=DB_HOST, 
            user=DB_USER, 
            password=DB_PASS, 
            database=DB_NAME, 
            connect_timeout=100000)
        print('[connnect] Iniciada la conexion a la DB')
        return conn
    except pymysql.MySQLError as e:
        print("[connect] Ha ocurrido una excepción: ", e)
        sys.exit()

# funcion para parametrizar los string de script.py
# en el parámetro *args podemos pasar tantos argumentos como queramos
# la función retorna una tupla con los argumentos ingresados
def return_tuple(*args):
    try:
        res  = (n for n in args)
        res_list = tuple(res)
        return res_list
    except Exception as e:
        print("[return_tuple] Ha ocurrido una excepcion: ", e)

# funcion para crear la tabla que necesites crear.  los argumentos
# que recibe son la conexion a la db y el query
def create_table(connection, query):
    try:
        cur = connection.cursor()
        cur.execute(query)
        connection.commit()
    except Exception as e:
        print("[create_table] Ha ocurrido una excepcion: ", e)
        return e

# funcion para crear un registro en la tabla elegida de la db.
# los argumentos que recibe son la conexion a la db, el query que quieres
# ejecutar, y la tupla con los valores para pasarle al query
def create_record(conn, query, data_tuple):
    try:
        cur = conn.cursor()
        cur.execute(query, data_tuple)
        conn.commit()
        return {
            "success": True,
            "message": "Se ha creado el registro en la DB"
        }
    except Exception as e:
        print("[create_table] Ha ocurrido una excepcion: ", e)
        return e

# ejemplo para crear tabla CLIENTS.
# CREATE_TABLE_CLIENTS esta en script.py
# se importa en la parte superior de este script
conn = connect()
# create_table(conn, CREATE_TABLE_CLIENTS)
# ejemplo para crear un regi

