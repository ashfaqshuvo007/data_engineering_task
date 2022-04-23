import requests
import logging
import sys
import psycopg2


from os import environ as env
from dotenv import load_dotenv
from db_operations import *
from db_connection import db_connection
load_dotenv()


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

url = env['API_URL']

headers = {
    "X-RapidAPI-Host": env['API_HOST'],
    "X-RapidAPI-Key":  env['API_KEY']
}
def import_data() -> None:
    try:
        #TODO: Connect to DB
        conn = db_connection()

        #TODO: PUll DATA
        try:
            response = requests.request("GET", url, headers=headers)
            
            data = response.json()
            if not data:
                logging.error("The request was unsuccessful!")
            else:
                #TODO:  if the request is successful
                logging.info("The request was a success!")
                #TODO: Create Table if not exists and insert data
                insert_data(conn,data)
                #TODO: DB insertion is successful
                logging.info("Data stored in DB successfully!")

        except requests.ConnectionError as error:
            logging.error(error)

    except psycopg2.Error as error:
        logging.error(error)

