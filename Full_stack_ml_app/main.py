from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import joblib
import pandas as pd
from pydantic import BaseModel

# Load ML Model
model = joblib.load("model.pkl")

# Class Labels
class_labels = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}

# Initialize FastAPI App
app = FastAPI()

# Serve Static Files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve Homepage (index.html)
@app.get("/")
def home():
    return FileResponse("static/index.html")

# Define Input Data Model
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float

# API Endpoint for Prediction
@app.post("/predict/")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    class_predictions = [class_labels[p] for p in prediction]
    return JSONResponse({"prediction": class_predictions})