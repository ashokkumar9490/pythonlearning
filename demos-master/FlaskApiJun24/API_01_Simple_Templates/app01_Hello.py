# Importing Flask module and creating a Flask web server from the Flask module
from flask import Flask
app = Flask(__name__)

# A decorator to tell Flask what URL should trigger the function hello()


@app.route('/hello', methods=['GET'])
def hello():
    # This function returns a JSON response with a greeting message
    return ({'message': 'Hello, Sharad!!!'})

# A decorator to tell Flask what URL should trigger the function error()


@app.route('/error', methods=['GET'])
def error():
    # This function triggers an error (division by zero)
    return 1/0


# Main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server. debug=True gives us
    # interactive debugging in the console.
    app.run(debug=True)
