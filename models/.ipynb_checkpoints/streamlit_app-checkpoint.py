 
import streamlit as st
import plotly.graph_objects as go
import requests

st.title("📈 AI-Powered Stock Prediction Dashboard")

# Fetch AI prediction from FastAPI
response = requests.get("https://your-render-api-url/predict")
predicted_price = response.json()["predicted_price"]

# Display AI forecast
st.subheader(f"🔮 Forecasted Stock Price: {predicted_price}")

# Plot stock trends
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Actual Prices", line=dict(color="blue")))
st.plotly_chart(fig)