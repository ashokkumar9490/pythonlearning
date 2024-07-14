import sys
from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "Store1", "items": [{"name": "Chair", "price": 15.99}]},
          {"name": "Store2", "items": [{"name": "Table", "price": 25.99}]}]


@app.get("/store")
def get_stores():
    print("getting stores")
    # sys.stdout.flush()
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    print("adding store - " + request_data['name'])
    # sys.stdout.flush()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


# @app.post("/store/<string:name>/item")
# def create_item(name):
#     request_data = request.get_json()
#     print(request_data)
#     for store in stores:
#         if store["name"] == name:
#             new_item = {
#                 "name": request_data["name"], "price": request_data["price"]}
#             store["items"].append(new_item)
#             return new_item, 201
#     return {"message": "Store not found"}, 404


@app.post("/store/<store_name>/item")             # make it post
def createItemInExistingStore(store_name):
    request_data = request.get_json()       # name and price of item
    # check if store with name passed is existing - it should exist
    store = [store for store in stores if store["name"] == store_name]
    if store:
        # check item name should not exist
        name = request_data["name"]
        price = request_data["price"]
        item = [item for item in store[0]["items"] if item["name"] == name]
        if (item):
            return {"message": "Item already exists"}, 500
        else:
            new_item = {"name": name, "price": price}
            store[0]["items"].append(new_item)
            return {"new item =": new_item}, 201

    return {"message": "Store name does not exists"}, 500


@app.get("/store/<string:name>")
def getStoreDetailsByName(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def getStoreItems(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)
