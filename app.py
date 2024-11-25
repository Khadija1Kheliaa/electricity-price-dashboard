"""
This is the main application file for the Streamlit dashboard. 
It fetches the electricity price data, processes it, and displays the results in a web-based dashboard when run locally.
"""

import streamlit as st
import pandas as pd
from data_fetch import fetch_data_for_next_24_hours
from data_processing import process_data
import matplotlib.pyplot as plt


st.title("📊 Electricity Price Dashboard")
st.write("")

raw_data = fetch_data_for_next_24_hours()
processed_data = process_data(raw_data)

# Notes section 
highest_price = processed_data['marketprice'].max()
time_maxprice = processed_data.loc[processed_data["marketprice"].idxmax(), 'time']

lowest_price = processed_data['marketprice'].min()
time_minprice = processed_data.loc[processed_data["marketprice"].idxmin(), 'time']

st.write("### 🔍 Key Insights:")
st.markdown(
    f"""
    - **Highest Price**: {highest_price:.2f} Eur/MWh at **{time_maxprice}**
    - **Lowest Price**: {lowest_price:.2f} Eur/MWh at **{time_minprice}**
    """
)

st.write("")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(processed_data['time'], processed_data['marketprice'], color='steelblue', edgecolor='black', width=0.8)

ax.set_title("Electricity prices over the next 24 Hours", color = 'darkblue',fontsize=20, fontweight='bold',pad=30  )

ax.set_xlabel("Start Time (Hour:Minute:Second)", fontsize=12, labelpad=10)
ax.set_ylabel("Price (Eur/MWh)", fontsize=12, labelpad=10)
ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
st.pyplot(fig)

# Data Table Below the Histogram
st.write("### 📋 Processed Data Table")
st.dataframe(processed_data)