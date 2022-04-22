import requests
import logging
import sys

from os import environ as env
from dotenv import load_dotenv
from database import *
load_dotenv()


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

url = env['API_URL']

headers = {
    "X-RapidAPI-Host": env['API_HOST'],
    "X-RapidAPI-Key":  env['API_KEY']
}

try:
    db_host=env['DB_HOST']
    db=env['DB']
    db_user=env['DB_USER']
    db_password=env['DB_PASSWORD']

    # Connect to DB
    conn = db_connect(db_host,db,db_user,db_password)

    # PUll DATA
    try:
        response = requests.request("GET", url, headers=headers)
        
        data = response.json()
        if not data:
            logging.error("The request was unsuccessful!")
        else:
            #  if the request is successful
            logging.info("The request was a success!")
            #Create Table if not exists and insert data
            insert_data(conn,data)
            #  if DB insertion is successful
            logging.info("Data stored in DB successfully!")

    except requests.ConnectionError as error:
        logging.error(error)

except psycopg2.Error as error:
    logging.error(error)

