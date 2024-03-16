import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import errorcode

# this will load environment variables stored in .env into your environment
load_dotenv()
# allows you to store password in .env or environment variable
my_password = str(os.environ.get('PASSWORD'))  

try:
    filmConnection = mysql.connector.connect(
        user="root",
        password=my_password,
        host='127.0.0.1',
        database='sakila'
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Invalid credentials')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database not found')
    else:
        print('Cannot connect to database', err)
else:
    filmCursor = filmConnection.cursor()

    filmQuery = ('SELECT * FROM actor')
    filmCursor.execute(filmQuery)
    for row in filmCursor.fetchall():
        print('Actor data', row[1], ' ', row[2])
    filmConnection.close()