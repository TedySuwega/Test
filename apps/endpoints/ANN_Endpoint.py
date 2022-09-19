import traceback

import uwsgi
from flask import json, make_response, request
from flask import current_app as app
from flask_restful import Resource
from werkzeug.exceptions import BadRequest, Unauthorized, NotFound, InternalServerError
from werkzeug.wrappers import Response

from apps.libs.model import ANNhandler
from apps.libs.validators import Validators

validators = Validators().get_validators()
headers_parser = validators["headers"]
root_parser = validators["root"]
data_parser = validators["data"]


class ANNModel(Resource):
    """
    Class for handling the Specialist Recommendations
    """

    def __init__(self):
        self.ANN_handler = ANNhandler()
        self.auth_unique_token = app.config["AUTH_UNIQUE_TOKEN"]

    def post(self) -> Response:
        try:
            print("to post req")
            if (
                "Auth-Unique-Token" not in request.headers.keys()
                or self.auth_unique_token != request.headers["Auth-Unique-Token"]
            ):
                app.logger.info(traceback.format_exc())
                raise Unauthorized

            # parse the request argument
            root_args = root_parser.parse_args()

            data = root_args["data"]
            print("datanya nih bree!!----------------------",data)

            # Predict ALL
            prediction = self.ANN_handler.predict_all(data)
            
            # Predict One
            prediction = self.ANN_handler.predict(data)

            res = {"data": {}}
            res["data"]["prediction"] = prediction
            return make_response(json.jsonify(res), 200)

        except Exception:
            app.logger.info(traceback.format_exc())
            uwsgi.set_logvar("requests", json.dumps(request.json))
            raise InternalServerError