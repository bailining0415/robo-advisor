

import requests
import sys
import json
#import pandas as pd
#from pandas.io.json import json_normalize
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv
import csv

dotenv_path = join(dirname(__file__), '.env')
data_path =  join(dirname(__file__), 'data')

if not os.path.isdir(data_path):
    os.mkdir(data_path)

load_dotenv(dotenv_path)

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}"

def validate_ticker(ticker):
    # TODO: Implement this
    pass

def output_ticker_data(ticker, json_data):
    with open(f"{data_path}/price_{ticker.lower()}.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        for k,v in json_data.items():
            row = [k]
            row = row + list(v.values())
            writer.writerow(row)

def to_usd(price):
    return "${0:,.2f}".format(price)


def recommand(latest_price, recent_high, recent_low):
    if latest_price >= recent_high:
        return "BUY"
    else:
        return "HOLD"


def reason_for_recommandation(action):
    if action == "BUY":
        return "Miss Bai think this is going to go up"
    elif action == "HOLD":
        return "Not a good time"

def recommand_for_ticker(ticker):

    response = requests.get(request_url.format(ticker, API_KEY))

    parsed_response = json.loads(response.text)

    if not 'Time Series (Daily)' in parsed_response:
        print(f"Sorry, cannot find any trading information for {ticker}. Please try another one.")
        sys.exit(1)

    data = parsed_response['Time Series (Daily)']
    metadata = parsed_response['Meta Data']

    output_ticker_data(ticker, data)

    latest_day = list(data)[0]

    latest = data[latest_day]
    latest_close = latest['4. close']
    recent_high = max([price['2. high'] for price in data.values()])
    recent_low =  min([price['3. low'] for price in data.values()])

    recommandation = recommand(latest_close, recent_high, recent_low)
    reason = reason_for_recommandation(recommandation)

    print("-------------------------")
    print("SELECTED SYMBOL: {}".format(ticker))
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST AT: {}".format(datetime.datetime.now()))
    print("-------------------------")
    print(f"LATEST DAY: {latest_day}")
    print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    print("-------------------------")
    print(f"RECOMMENDATION: {recommandation}!")
    print(f"RECOMMENDATION REASON: {reason}")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")


raw_input = input("Please enter tickers (e.g. MSFT or MSFT, AAPL): ")
tickers = [ticker.strip() for ticker in raw_input.split(",")]


for ticker in tickers:
    validate_ticker(ticker)
    recommand_for_ticker(ticker) 
