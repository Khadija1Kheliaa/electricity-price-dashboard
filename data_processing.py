"""
(Optional) This file contains data processing functions such as cleaning, normalizing, or further transforming the fetched electricity price data before it is visualized.
"""

import pandas as pd
from datetime import datetime
from data_fetch import fetch_data_for_next_24_hours

def process_data(raw_data) :

    # Initialize lists to store processed data
    timestamps = []
    prices = []

    for  item in raw_data['data'] :  # we acces a key called data in the dictionnary rawdata
       
       start_timestamp = item['start_timestamp']
       market_price = item['marketprice']

       # Convert the timestamp to a human-readable time format
       start_time = datetime.utcfromtimestamp(start_timestamp/1000) #convert from milleseconds to seconds
       
       # Format the time into a string  to show only hour, minute, and second
       readable_time = start_time.strftime('%H:%M:%S')
       
       timestamps.append(readable_time)
       prices.append(market_price)

    # Create a DataFrame from the lists
    # a dictionnary {} is passed as an argument , each key in the dictionnary 
    # becomes a column name

    df = pd.DataFrame({
    'time': timestamps,         # Column 1: 'time' 
    'marketprice': prices       # Column 2: 'marketprice'
    })


    return df

