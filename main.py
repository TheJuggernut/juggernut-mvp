import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

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

# Options Income Tracker
st.subheader("Options Income Tracker")
options_data = pd.DataFrame({
    "Ticker": ["AAPL", "TSLA", "NVDA"],
    "Type": ["Call", "Put", "Call"],
    "Strike": [190, 250, 420],
    "Expiration": ["2025-08-15", "2025-08-22", "2025-09-05"],
    "Premium ($)": [250, 320, 210],
    "Current Value ($)": [120, 400, 190],
    "Days Until Expiration": [
        (datetime.strptime("2025-08-15", "%Y-%m-%d") - datetime.today()).days,
        (datetime.strptime("2025-08-22", "%Y-%m-%d") - datetime.today()).days,
        (datetime.strptime("2025-09-05", "%Y-%m-%d") - datetime.today()).days,
    ]
})
st.dataframe(options_data)

# Alert Logic
alerts = []
today = datetime.today()
for _, row in options_data.iterrows():
    days_left = (datetime.strptime(row['Expiration'], "%Y-%m-%d") - today).days
    if days_left <= 3:
        alerts.append(f"⚠ {row['Ticker']} {row['Type']} expiring in {days_left} day(s) ({row['Expiration']})")
    if row['Type'] == "Call" and row['Strike'] < 200:
        alerts.append(f"📈 {row['Ticker']} Call strike {row['Strike']} approaching!")

if alerts:
    st.warning("\n".join(alerts))

# Goal Tracker
st.subheader("Goal Tracker")
goal = 1_000_000
current_value = np.random.randint(50_000, 250_000)
st.metric(label="Portfolio Value", value=f"${current_value:,}", delta=f"{(current_value/goal*100):.2f}% to goal")
st.progress(current_value/goal)

# AI Suggestion Placeholder
st.markdown("**AI Suggestion:** Increase allocation to outperforming sectors, "
            "consider options strategies for TSLA/NVDA based on volatility breakout.")
