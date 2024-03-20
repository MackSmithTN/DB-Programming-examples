# an object of WSGI application 
from flask import Flask

app = Flask(__name__) # Flask constructor 

# A decorator used to tell the application 
# which URL is associated with what function 
@app.route('/hello')	 
def hello(): 
	return 'HELLO'

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(port=8000, debug=True)