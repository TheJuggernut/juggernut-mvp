
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Juggernut MVP", layout="wide")

st.title("🚀 Juggernut MVP Dashboard")
st.markdown("### Apple-Clean UI • NVDA-Powerful Insights")

# Rip Radar
st.subheader("Rip Radar (Mock Data)")
rip_data = pd.DataFrame({
    "Ticker": ["AAPL", "TSLA", "AMD", "NVDA", "MSFT"],
    "Rip Start": ["09:45", "10:05", "09:50", "10:15", "09:55"],
    "% Since Rip": np.random.uniform(0.5, 5, 5).round(2)
})
st.dataframe(rip_data)

# Sector Surge
st.subheader("Sector Surge (Mock)")
sector_data = pd.DataFrame({
    "Sector": ["Tech", "Energy", "Healthcare", "Finance", "Utilities"],
    "Sector Gain %": np.random.uniform(-0.5, 2, 5).round(2),
    "SPY Comparison %": np.random.uniform(-0.3, 1.5, 5).round(2)
})
st.dataframe(sector_data)

# Goal Tracker
st.subheader("Goal Tracker")
goal = 1000000
current_value = np.random.randint(50000, 250000)
st.metric(label="Portfolio Value", value=f"${current_value:,}", delta=f"{(current_value/goal*100):.2f}% to goal")

st.progress(current_value/goal)

# AI Suggestion Placeholder
st.markdown("**AI Suggestion:** Increase allocation to outperforming sectors, consider options strategies for TSLA/NVDA based on volatility breakout.")
