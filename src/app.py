
from math import ceil, floor
from urllib import response
import psycopg2
import logging
import json

from flask import Flask, jsonify,request
from db_connection import db_connection
from db_operations import get_data
from import_data import import_data
from datetime import datetime as dt


app = Flask(__name__)


#TODO: Root Route
@app.route('/')
def index():
    response_dict = {
        'status': 200,
        'message': 'App is Live!'
    }
    return jsonify(response_dict)



#TODO: Show DB data Route
@app.route('/show_data', defaults={'page': 1})
@app.route('/show_data/<page>')
def show_data(page):
    conn = db_connection()
    page = request.args.get('page', type=int, default=int(page))

    #TODO: Pull data with pagination 
    try:
        response_dict = get_data(page,conn)
    except psycopg2.Error as error:
        logging.error(error)
        response_dict = {
                'status': 404,
                'error': error
        }
    return jsonify(response_dict)



#TODO: Pulling Live data from API Route
@app.route('/load_data')
def load_data():
    import_data()
    logging.info("New data Loaded")
    timestamp_str = dt.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    response_string = 'New data pulled at {time}'.format(time=timestamp_str)
    response_dict = {
                'status': 200,
                'message': response_string
        }
    return jsonify(response_dict)



if __name__ == '__main__':
    app.run(debug=True,port=5000)