# import necessary libraries
import pandas as pd
import numpy as np
import requests as rq

# yahoo finance url
url = 'https://query1.finance.yahoo.com/v8/finance/chart/AAPL'

# parameters
params = {
    "range": "1mo",
    "interval": "1d",
    "region": "US",
    "lang": "en-US",
    "includePrePost": False,
    "events": "div, splits"
}

# header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# use requests to hit yahoo API
response = rq.get(url, params, headers= headers)


# check if the api is responding
if response.status_code == 200:
    data = response.json()
    timestamps = data['chart']['result'][0]['timestamp']
    price = data['chart']['result'][0]['indicators']['quote'][0]


    # convert the json data into a dataframe
    dataset = pd.DataFrame({
        'Datetime': pd.to_datetime(timestamps, unit='s'),
        'Open': price['open'],
        'High': price['high'],
        'Low': price['low'],
        'Close': price['close'],
        'Volume': price['volume']
    })
    print(dataset.head(10))
else:
    print("Failed to fetch data", response.status_code)
# print shape of dataset
print(dataset.shape)
