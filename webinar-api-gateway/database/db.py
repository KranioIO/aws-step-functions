import pymysql
import os
import sys

# dejar como variable de entorno y si hay tiempo usar ssm
DB_USER = os.getenv('db_user')
DB_PASS = os.getenv('db_pass')
DB_NAME= os.getenv('db_name')
DB_PORT = os.getenv('db_port')
DB_HOST = os.getenv('db_host')

def connect():
    try:
        conn = pymysql.connect(
            host=DB_HOST, 
            user=DB_USER, 
            password=DB_PASS, 
            database=DB_NAME, 
            connect_timeout=100000)
        print('connected')
        return conn
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()

def return_tuple(*args):
    try:
        res  = (n for n in args)
        res_list = tuple(res)
        return res_list
    except Exception as e:
        print(e)

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
        print("create record exception: ", e)
        return e
        # return {
        #     "success": False,
        #     "message": e
        # }
        
def create_table(connection, query):
    try:
        cur = connection.cursor()
        cur.execute(query)
        connection.commit()
    except Exception as e:
        print(e)

# conn = connect()
# create_table(conn, CREATE_TABLE_CLIENTS)
# create_table(conn, CREATE_TABLE_PARTNERS)
# create_table(conn, CREATE_TABLE_BENEFITS)

