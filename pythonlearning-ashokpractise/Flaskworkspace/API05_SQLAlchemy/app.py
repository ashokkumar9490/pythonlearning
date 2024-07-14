from flask_smorest import Api
from flask import Flask, request, jsonify
import os
from db import db
from flask_migrate import Migrate
# from resources2.store import store_blp
# from resources2.item import item_blp
# from resources.store import store_blp
# from resources.item import item_blp
from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint

app = Flask(__name__)
#this is for swagger ui
app.config["API_TITLE"] = "Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# app.config["SQLALCHEMY_DATABASE_URI"] =  os.getenv(
#         "DATABASE_URL", "sqlite:///data.db")
    # create mysql database
app.config["SQLALCHEMY_DATABASE_URI"] =  os.getenv(
   'DATABASE_URL', 'mysql+pymysql://root:root@localhost:3306/stores_db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # type: ignore
api = Api(app)

migrate = Migrate(app, db)
# Create all tables in the database before starting the server
# with app.app_context():
#     db.create_all() # type: ignore
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)