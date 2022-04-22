## A Simple ETL Pipeline:
## Steps:
    1. Environment Setup
        - python3 -m venv venv
        - source venv/bin/activate
        - pip install -r requirements.txt
    2. DB Setup (postrgres)
        - Login to postgres
            - psql -U userName
            - Enter your password when prompted.
        - Create DB
            - CREATE DATABASE myDatabase WITH ENCODING 'UTF8' LC_COLLATE='English_United Kingdom' LC_CTYPE='English_United Kingdom';
        - Create User
            - create user user_name with encrypted password 'mypassword';
        - Grant All privileges to user for the db
            - grant all privileges on database myDatabase to user_name;
    3.  Run importData.py to pull and store data in the database
        - python importData.py