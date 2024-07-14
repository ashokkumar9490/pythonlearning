# import uuid
# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from flask import request
# from db import items
# from schemas import ItemSchema, ItemUpdateSchema
# item_blp = Blueprint("Items", __name__, description="Operations on items")

# @item_blp.route("/item")
# class Store(MethodView):
#     @item_blp.response(200, ItemSchema(many=True))
#     def get(self):
#         print(list(items.values()))
#         return list(items.values())
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import request
from db import items
from schemas import ItemSchema, ItemUpdateSchema
item_blp = Blueprint("Items", __name__, description="Operations on items")
@item_blp.route("/item/<string:item_id>")
class Item(MethodView):
    @item_blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")
    @item_blp.arguments(ItemUpdateSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found.")
@item_blp.route("/item")
class ItemList(MethodView):
    @item_blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()
# after implementing marshmallow schemas
    @item_blp.arguments(ItemSchema)
    @item_blp.response(201, ItemSchema)
    def post(self, item_data):
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