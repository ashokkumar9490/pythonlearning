import uuid
from flask_smorest import Api
from flask import Flask, abort, request, jsonify
from db import stores, items

app = Flask(__name__)

# remove nested collection
# added a separate set of collection in separate file
# to represent database
# and changed list to dictionary -
# id will be key and values will be having all data


@app.get("/store")
def get_stores():
    return {"My stores": list(stores.values())}


# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store

#     return store


if __name__ == '__main__':
    app.run(debug=True)


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404


@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        print('store name not found in request data')
        abort(
            400,
            "Bad request. Ensure name is included in the JSON payload.",
        )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            print('store already exists')
            abort(400, "Store already exists.")

    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store


# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if item_data["store_id"] not in stores:
#         return {"message": "Store not found"}, 404

#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item

#     return item


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
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message=f"Item already exists.")

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
        abort(404, message="Store not found.")
        # return {"message": "Item not found"}, 404


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Item not found.")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    # There's  more validation to do here!
    # Like making sure price is a number, and also both items are optional
    # You should also prevent keys that aren't 'price' or 'name' to be passed
    # Difficult to do with an if statement...
    if "price" not in item_data or "name" not in item_data:
        abort(
            400,
            message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
        )
    try:
        item = items[item_id]
        item |= item_data  # item.update(item_data)

        return item
    except KeyError:
        abort(404, message="Item not found.")


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message="Store not found.")


# removed as using db
# stores = [
#     {
#         "name": "Store 1",
#         "items": [
#             {
#                 "name": "Chair",
#                 "price": 15.99}
#         ]}
# ]


# @app.get("/store")
# def get_stores():
#     return {"stores": stores}


# @app.get("/store/<string:name>")
# def get_store(name):
#     for store in stores:
#         if store["name"] == name:
#             return store
#     return {"message": "Store not found"}, 404


# @app.get("/store/<string:name>/item")
# def get_item_in_store(name):
#     for store in stores:
#         if store["name"] == name:
#             return {"items": store["items"]}
#     return {"message": "Store not found"}, 404


# @app.post("/store")
# def create_store():
#     request_data = request.get_json()
#     new_store = {"name": request_data["name"], "items": []}
#     stores.append(new_store)
#     return new_store, 201


# @app.post("/store/<string:name>/item")
# def create_item(name):
#     request_data = request.get_json()
#     print(request_data)
#     for store in stores:
#         if store["name"] == name:
#             new_item = {
#                 "name": request_data["name"], "price": request_data["price"]}
#             store["items"].append(new_item)
#             return new_item
#     return {"message": "Store not found"}, 404
