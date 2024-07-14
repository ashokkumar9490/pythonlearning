from flask import Flask, request
app = Flask(__name__)
stores = [
    {
        "name" : "Store 1",
        "items":[
            {
                "name" : "Table",
                "price": 5678
            },
            {
                "name" : "Chair",
                "price": 567
            },
        ]
    },
    {  
        "name" : "Store 2",
        "items":[
            {
                "name" : "Laptop",
                "price": 45000
            },
            {
                "name" : "Tab",
                "price": 5670
            },
        ]
    }
]
@app.route("/store")
def getStores():
    return {"stores": stores}
 
@app.post("/store")
def createStore():
    request_data = request.get_json()
    name = request_data[ name ]
    store = [store for store in stores if store["name"] == name]
    # check if the store with name passed is existing
    for store in stores:
        if store["name"] == name:
            return ["Error Store is Existing"], 500
    new_store = { "name": request_data["name"], "items": []}
    stores.append(new_store)
    return {"new store =":new_store}, 201
 
@app.post("/store/<store_name>/item")
def createItemInExistingStore(store_name):  
    request_data = request.get_json()    
    name = request_data["name"]
    store = [store for store in stores if store["name"] == store_name]
    if store:
        name = request_data["name"]
        price = request_data["price"]
        item = [item for item in store[0]["items"] if item["name"] == name]
        if(item):
            return {"message": "Item already exists"}, 500
        else:
            new_item = {"name": name, "price": price}    
            store[0]["items"].append(new_item)
            return {"new item =":new_item}, 201      
    #return {"new store =":new_item}, 201
    return {"message":"store name does not exists"}, 500

@app.get("/store/<string:name>") 
def getStoreByName(name):
    for store in stores:
        if store["name"] == name:
            return {"store details" : store}
        return {"message": "store not found"}, 404
    
@app.get("/store/<string:name>/item") 
def getItemsFromStore(name):
    for store in stores:
        if store["name"] == name:
            return {"items" : store["items"]}
        return {"message": "store not found"}, 404    

