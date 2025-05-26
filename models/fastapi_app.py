 
from fastapi import FastAPI
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

app = FastAPI()
model = load_model("optimized_model.h5")  # Load AI model

@app.get("/predict")
def get_prediction():
    latest_data = pd.read_csv("daily_backup.csv")
    latest_price = latest_data["Close"].values[-60:]  # Last 60 closing prices
    latest_price_scaled = scaler.transform(latest_price.reshape(-1, 1))

    predicted_price = model.predict(latest_price_scaled.reshape(1, 60, 1))
    predicted_price = scaler.inverse_transform(predicted_price)

    return {"predicted_price": float(predicted_price[0][0])}