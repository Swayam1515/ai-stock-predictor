import os
import streamlit as st
import requests

# 🔥 Set Render's expected port dynamically
port = os.getenv("PORT", 10000)

# ✅ Streamlit App UI
st.set_page_config(page_title="TickerAI - Stock Predictor 🚀")

st.title("📈 AI-Powered Stock Prediction")
st.write(f"Server running on port {port}")

# 📌 Correct API URL (replace with your actual endpoint)
API_URL = "https://ai-stock-predictor-fcgq.onrender.com/predict"

# 🎯 User Input for Stock Ticker
ticker = st.text_input("Enter a stock ticker (e.g., AAPL, TSLA)")

if ticker:
    try:
        # 🚀 API Request to Backend
        response = requests.get(f"{API_URL}?ticker={ticker}")

        # ✅ Check Response Status
        if response.status_code == 200:
            data = response.json()
            st.subheader(f"Stock Prediction for {ticker}:")
            st.write(data)
        else:
            st.error("⚠️ Error fetching prediction. Try again later.")
    
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection error: {e}")