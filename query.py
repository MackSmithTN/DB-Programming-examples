# an object of WSGI application 
from flask import Flask, request	 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
from dotenv import load_dotenv

load_dotenv()
my_password = str(os.environ.get('PASSWORD'))

app = Flask(__name__) # Flask constructor 
db_cred = { 
    'user': 'root',         # DATABASE USER 
    'pass': my_password,    # DATABASE PASSWORD 
    'host': '127.0.0.1:3306',    # DATABASE HOSTNAME 
    'name': 'sakila'        # DATABASE NAME 
} 
db_uri = f"mysql+pymysql://{db_cred['user']}:{db_cred['pass']}@{db_cred['host']}/{db_cred['name']}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# A decorator used to tell the application 
# which URL is associated function 
@app.route('/hello')	 
def hello(): 
	return 'HELLO'

# APP ROUTE TO GET RESULTS FOR SELECT QUERY 
@app.route('/get_actors', methods=['POST']) 
def get_actors(): 
      
    # GET THE SQLALCHEMY RESULTPROXY OBJECT 
    with db.engine.begin() as conn: 
        result = conn.execute(text(request.get_json()['query'])) 
    response = {} 
    i = 1
  
    # ITERATE OVER EACH RECORD IN RESULT AND ADD IT  
    # IN A PYTHON DICT OBJECT 
    for each in result: 
        response.update({f'Record {i}': list(each)}) 
        i+= 1
  
    return response 

if __name__=='__main__': 
    app.run(port=8000, debug=True) 
