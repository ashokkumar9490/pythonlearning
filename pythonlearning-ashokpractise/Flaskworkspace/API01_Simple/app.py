from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def SayHello():
    return ({'message': 'Hello World'})

@app.route('/hi')
def SayHi():
    return ({'message': 'Hi from flask app'})

@app.route('/error')
def CheckError():
    return 10 / 0
