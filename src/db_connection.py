"""Import Necessary modules"""
import logging
from os import environ as env
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def db_connection():
    db_host=env['DB_HOST']
    db_conn=env['DB']
    db_user=env['DB_USER']
    db_password=env['DB_PASSWORD']
    connection = psycopg2.connect(
        host=db_host,
        database=db_conn,
        user=db_user,
        password=db_password,
    )
    connection.autocommit = True
    logging.info("DB Connection was a success!")

    return connection
