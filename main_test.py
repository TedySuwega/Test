
from pipeline.Trainer.training import ANN
import numpy as np
import pickle
from tensorflow.keras.models import load_model

data = [0.07748055, 0.07941484, 0.0885422, 0.08627246]

# /home/tedy/Documents/Tedy_Suwega_Learning_Report/Sandbox/model/model.pkl
# cf = ANN()
# model = cf._training_model("model/")

def load_model_ann():
    # load model
    model = load_model("model/")
    return model


model = load_model_ann()
pickled_prediction = model.predict(np.array([data]))
predict_label = np.argmax(pickled_prediction, axis=1)
print("predict_prediction = ", predict_label)