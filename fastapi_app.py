from fastapi import FastAPI
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from fastapi.middleware.cors import CORSMiddleware
import os  # ✅ For dynamic port binding

import sys
sys.path.append(".")  # ✅ Ensures Python finds modules in the current directory

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Enable CORS to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Load AI model
model = load_model("optimized_model.h5")

# 🔥 Initialize scaler
scaler = MinMaxScaler()

# 🔥 Load & preprocess data (Ensure `daily_backup.csv` exists)
latest_data = pd.read_csv("daily_backup.csv")

# ✅ Train scaler using historical closing prices
scaler.fit(latest_data[["Close"]])

@app.get("/predict")
def get_prediction():
    # 📌 Extract last 60 closing prices
    latest_price = latest_data["Close"].values[-60:]
    latest_price_scaled = scaler.transform(latest_price.reshape(-1, 1))

    # 🚀 Predict stock price
    predicted_price = model.predict(latest_price_scaled.reshape(1, 60, 1))
    predicted_price = scaler.inverse_transform(predicted_price)

    return {"predicted_price": float(predicted_price[0][0])}

# ✅ Bind to Render's required port dynamically
if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Render provides PORT as an env variable
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)