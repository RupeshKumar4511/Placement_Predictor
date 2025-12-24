import pickle
import pandas as pd 

# Function to load ml model
def load_model():
    with open('./model/model.pkl','rb+') as f : 
        model = pickle.load(f)
    return model

# Function to load scaler (StandardScaler)
def load_scaler():
    with open('./model/scaler.pkl','rb+') as f : 
        scaler = pickle.load(f)
    return scaler


MODEL_VERSION = '1.0.0'


def predict_output(data):
    model = load_model() 
    x_new = pd.DataFrame(dict(data),index=[0])
    scaler = load_scaler()
    x_new_scaled = scaler.transform(x_new)
    predict = model.predict(x_new_scaled)
    return predict