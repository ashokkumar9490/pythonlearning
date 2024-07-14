from flask_smorest import Api
from flask import Flask, request, jsonify
from resources.store import store_blp
from resources.item import item_blp
app = Flask(__name__)
app.config["API_TITLE"] = "Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(item_blp)
api.register_blueprint(store_blp)