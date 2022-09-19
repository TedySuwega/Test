import joblib
import traceback
from decimal import Decimal

# import pickle

from flask import current_app as app
import numpy as np
from pandas import DataFrame
from werkzeug.exceptions import NotFound

from tensorflow.keras.models import load_model


class ANNHandler:
    """
    Class for handling the specialist categories' recommender model.
    """

    def __init__(self, model_path: str = None, label_path: str = None):
        """
        Class' variables initialization process.
        """
        self.__load_model(model_path)

    def __load_model(self, model_path):
        """
        Load model.
        """
        try:
            self.model: object = load_model(model_path)
            app.logger.info("LOAD MODEL")
        except ValueError:
            return traceback.format_exc()
        except NotFound:
            return traceback.format_exc()
        except KeyError:
            return traceback.format_exc()

    def predict_all(self, data):
        pickled_prediction = self.model.predict(np.array([data]))
        predict_label = np.argmax(pickled_prediction, axis=1)
        # print("predict_prediction = ", predict_label)
        return predict_label

    def predict_one(self, data):
        pickled_prediction = self.model.predict(np.array([data[0]]))
        predict_label = np.argmax(pickled_prediction, axis=1)
        # print("predict_prediction = ", predict_label)
        return predict_label