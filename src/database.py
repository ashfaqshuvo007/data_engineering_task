from csv import excel_tab
import psycopg2
import logging

# Connect to db
def db_connect(db_host,db,db_user,db_password):
    connection = psycopg2.connect(
        host=db_host,
        database=db,
        user=db_user,
        password=db_password,
    )
    connection.autocommit = True
    logging.info("DB Connection was a success!")

    return connection

#create DB table
def create_db_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS etl_crypto_data;
        CREATE UNLOGGED TABLE etl_crypto_data (
            id                           VARCHAR PRIMARY KEY,
            name                         VARCHAR NOT NULL,
            description                  TEXT,
            adjusted_rank                INTEGER,
            reported_rank                INTEGER,
            currencies                   INTEGER,
            markets                      INTEGER,
            quote_usd_reported_24h       DECIMAL,
            quote_usd_adjusted_24h       DECIMAL,
            quote_usd_reported_7d        DECIMAL,
            quote_usd_adjusted_7d        DECIMAL
        );
    """)

#Insert data into table
def insert_data(connection, data) -> None:
    create_db_table(connection)

    all_data = [{
        **d,
        'quote_usd_reported_24h': d['quotes']['USD']['reported_volume_24h'],
        'quote_usd_adjusted_24h': d['quotes']['USD']['adjusted_volume_24h'],
        'quote_usd_reported_7d': d['quotes']['USD']['reported_volume_7d'],
        'quote_usd_adjusted_7d': d['quotes']['USD']['adjusted_volume_7d']
    } for d in data]

    cursor = connection.cursor()
    cursor.executemany("""
        INSERT INTO etl_crypto_data VALUES (
            %(id)s,
            %(name)s,
            %(description)s,
            %(adjusted_rank)s,
            %(reported_rank)s,
            %(currencies)s,
            %(markets)s,
            %(quote_usd_reported_24h)s,
            %(quote_usd_adjusted_24h)s,
            %(quote_usd_reported_7d)s,
            %(quote_usd_adjusted_7d)s
        );
    """, all_data)