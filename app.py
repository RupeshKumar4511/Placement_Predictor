from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import Student
from model.predict import predict_output,MODEL_VERSION


# create an instance of FastAPI
app = FastAPI()



# create routes
@app.get('/')
def home():
    return {"message":"Student Placement Predictor API"}


@app.get('/health')
def health():
    return {"status":"OK",
            "model_version":MODEL_VERSION}


@app.post('/predict')
def predict_placement(data:Student):
    try:
        predict = predict_output(data)
        if(predict[0]==1):
            return {"placed":"Yes"}
        else:
            return {"placed":"No"}
    except Exception as e:
        raise JSONResponse(status_code=500,content=str(e))

    
