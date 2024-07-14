from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/EmpsDB"
mongo = PyMongo(app)


@app.route("/emps")
def home_page():
    # emps = mongo.db.Emps.find()
    print([x for x in mongo.db.Emps.find({})])
    return jsonify([i for i in mongo.db.Emps.find({}, {'_id': 0})])


@app.post("/emps")
def add_emp():
    emp = request.get_json()
    # emp = {"Name": "Ravi", "Salary": 30789}
    mongo.db.Emps.insert_one(emp)
    return "Added Successfully"
