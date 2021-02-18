"""
script con statements SQL parametrizables para crear las tablas
"""

CREATE_TABLE_CLIENTS = """ 
    CREATE TABLE IF NOT EXISTS CLIENTS 
    (name varchar(25), 
    lastname varchar(25), 
    rut varchar(25), 
    mail varchar(25), 
    phone varchar(25)); """

CREATE_TABLE_PARTNERS = """ 
    CREATE TABLE IF NOT EXISTS PARTNERS 
    (rut varchar(25), 
    store varchar(25)); """

CREATE_TABLE_BENEFITS = """ 
    CREATE TABLE IF NOT EXISTS BENEFITS 
    (rut varchar(25), 
    wantsBenefit boolean not null default 0); """

SELECT_ALL_CLIENTS = """ SELECT * FROM CLIENTS """
SELECT_ALL_PARTNERS = """ SELECT * FROM PARTNERS """
SELECT_ALL_BENEFITS = """ SELECT * FROM BENEFITS """

INSERT_CLIENT = """ 
    INSERT INTO CLIENTS 
    (name, lastname, rut, mail, phone) 
    VALUES (%s, %s, %s, %s, %s) """

INSERT_PARTNER = """ 
    INSERT INTO PARTNERS (rut, store) 
    VALUES (%s, %s) """

INSERT_BENEFIT = """ 
    INSERT INTO BENEFITS (rut, wantsBenefit) 
    VALUES (%s, %s) """
