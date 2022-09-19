import os

from flask import Flask, current_app
from flask_restful import Api
from simplejson import JSONEncoder, JSONDecoder
from apps.endpoints.ANN_Endpoint import ANNModel
from apps.helpers import errors

app = Flask(__name__)
api = Api(app, errors=errors)
app.json_encoder = JSONEncoder
app.json_decoder = JSONDecoder

app.config.from_pyfile("./instance/instance.cfg")


model_path = app.config["MODEL_PATH"]

api.add_resource(ANNModel, "/api_ANN")