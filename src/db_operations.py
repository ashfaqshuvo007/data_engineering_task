"""Import Necessary modules"""
from datetime import datetime as dt
from math import floor

# create DB table
def create_db_table(connection) -> None:
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
            quote_usd_reported_24h       FLOAT,
            quote_usd_adjusted_24h       FLOAT,
            quote_usd_reported_7d        FLOAT,
            quote_usd_adjusted_7d        FLOAT,
            last_updated                 VARCHAR NOT NULL
        );
    """)

# Insert data into table
def insert_data(connection, data) -> None:
    create_db_table(connection)
    timestamp_str = dt.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    all_data = [{
        **d,
        'quote_usd_reported_24h': d['quotes']['USD']['reported_volume_24h'],
        'quote_usd_adjusted_24h': d['quotes']['USD']['adjusted_volume_24h'],
        'quote_usd_reported_7d': d['quotes']['USD']['reported_volume_7d'],
        'quote_usd_adjusted_7d': d['quotes']['USD']['adjusted_volume_7d'],
        'last_updated': timestamp_str
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
            %(quote_usd_adjusted_7d)s,
            %(last_updated)s
        );
    """, all_data)

# Get Rows from DB
def get_data(page,connection) -> dict:

    # Total Data
    cur = connection.cursor()
    cur.execute('SELECT COUNT(*) from etl_crypto_data')
    results = cur.fetchone()
    for r_data in results:
        total_count = r_data
    if page==1:
        cur.execute('SELECT * from etl_crypto_data ORDER BY id'
                    + 'ASC LIMIT {limit} offset {offset}'
                        .format(limit = 25, offset = 0))
        data = cur.fetchall()
    else:
        cur.execute('SELECT * from etl_crypto_data ORDER BY id'
                    + 'ASC LIMIT {limit} offset {offset}'
                    .format(limit = 25, offset = (5 * int(page))))
        data = cur.fetchall()


    response_dict = {
        'status': 200,
        'message': 'Showing 25 rows',
        'page': page,
        'total_pages': floor(total_count/25),
        'data': data
    }
    return response_dict
