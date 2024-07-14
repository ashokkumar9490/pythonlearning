import sys
from flask import Flask, request
import logging
app = Flask(__name__)

logger = logging.getLogger('werkzeug')  # grabs underlying WSGI logger
handler = logging.FileHandler('test.log')  # creates handler for the log file
logger.addHandler(handler)  # adds handler to the werkzeug WSGI logger


stores = [{"name": "Store1", "items": [{"name": "Chair", "price": 15.99}]},
          {"name": "Store2", "items": [{"name": "Table", "price": 25.99}]}]


@app.get("/store")
def get_stores():
    logger.info("Here's some info")
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    print("adding store - " + request_data['name'])
    sys.stdout.flush()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)
