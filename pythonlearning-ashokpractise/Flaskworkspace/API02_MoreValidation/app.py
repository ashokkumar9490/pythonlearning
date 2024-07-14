import uuid
#uuid is generate unique ids
from flask_smorest import Api
from flask import Flask, abort, request, jsonify
from db import stores, items

app = Flask(__name__)

@app.get("/store")
def get_stores():
    return {"My stores": list(stores.values())}

#create endpont for - Get store by id
@app.get("/store/<string:store_id>")
def get_store(store_id):

    try:
        return stores[store_id]
    except KeyError:
        return {"message": "store not found"}, 404
    
# try to fetch in different way     
    # store = stores.get(store_id)
 
    # if not store:
    #     abort(404, "Store with ID {store_id} not found")
 
    # return jsonify(store)

# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        print('store name not found in request data')
        abort(
            400,
            "Bad request. Ensure 'name' is included in the JSON payload.",
        )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            print('store already exists')
            abort(400, "Store already exists.")
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store

@app.post("/item")
def create_item():
    item_data = request.get_json()
    # Here not only we need to validate data exists,
    # But also what type of data. Price should be a float,
    # for example.
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            "Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, "Item already exists.")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, "Store not found.")
        # return {"message": "Item not found"}, 404
# try to create delete endpoint for item
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
         del items[item_id]
         return { "message": "item id deleted"}
    except  KeyError :
         abort(404, "item not found.")    

# try to create delete endpoint for store   
@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
         del stores[store_id]
         return { "message": "store id deleted"}
    except  KeyError :
         abort(404, "store not found.")  
         
@app.put("/item/<item_id>")
def update_item_by_id(item_id):
    updated_data =  request.get_json()
    items[item_id].update(updated_data)
    return jsonify(items[item_id])