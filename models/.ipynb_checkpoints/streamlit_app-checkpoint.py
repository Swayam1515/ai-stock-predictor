import streamlit as st
import pandas as pd
import requests

# Set Streamlit page config
st.set_page_config(page_title="Stock Price Prediction", layout="wide")

# Title & Description
st.title("📈 Stock Price Prediction Dashboard")
st.write("🚀 Enter a stock ticker and get AI-powered price predictions!")

# Input for Stock Ticker
ticker = st.text_input("Enter Stock Ticker:", "AAPL")

# Fetch Prediction from FastAPI
if st.button("Get Prediction"):
    try:
        response = requests.get(f"http://localhost:10000/predict?ticker={ticker}")
        predicted_price = response.json().get("predicted_price", "Error fetching prediction")
        st.success(f"💰 Predicted Price for {ticker}: ${predicted_price:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")

# Load and Display Historical Data
try:
    df = pd.read_csv("daily_backup.csv")

    # Ensure proper formatting
    df["Date"] = pd.to_datetime(df["Date"])  # Convert date format
    df = df.sort_values("Date", ascending=False)  # Sort by recent date

    st.subheader("📊 Historical Stock Prices")
    st.dataframe(df)

    # Plot historical prices
    st.line_chart(df.set_index("Date")["Close"])
except Exception as e:
    st.error(f"⚠️ Error loading historical data: {e}")

# Footer
st.write("🔍 **FastAPI + Streamlit Integration by Swayam** | 🚀 Powered by AI")