# import uuid
# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from db import stores
# from flask import request
# from schemas import StoreSchema
# store_blp = Blueprint("Stores", __name__, description="Operations on stores")

# @store_blp.route("/store")
# class StoreList(MethodView):
#     @store_blp.response(200, StoreSchema(many=True))
#     def get(self):
#         print(list(stores.values()))
#         return list(stores.values())
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from flask import request
from schemas import StoreSchema
store_blp = Blueprint("Stores", __name__, description="Operations on stores")
@store_blp.route("/store/<string:store_id>")
class Store(MethodView):
    @store_blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
@store_blp.route("/store")
class StoreList(MethodView):
    @store_blp.response(200, StoreSchema(many=True))
    def get(self):
        return {"stores": list(stores.values())}
    @store_blp.arguments(StoreSchema)
    @store_blp.response(201, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists.")
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store