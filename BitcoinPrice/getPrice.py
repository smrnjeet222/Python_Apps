# Track Bitcoin prices Live

import requests
import os

os.system("cls")

URL = 'https://blockchain.info/ticker'


def scrape(CURRENCY):
    response = requests.get(URL)
    response_json = response.json()
    return (response_json[CURRENCY]['last'])


last_price = None

currency = ["USD", "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "DKK", "EUR",
            "GBP", "HKD", "INR", "ISK", "JPY", "KRW", "NZD", "PLN", "RUB", "SEK",
            "SGD", "THB", "TRY", "TWD"]

cur = currency[11]

while True:
    latest_price = scrape(cur)
    if latest_price != last_price:
        print(f"Latest Price of bitcoin :",
              "\u001b[31;1m", cur, latest_price, "\u001b[0m")
        last_price = latest_price
