import os
import requests
from twilio.rest import Client

STOCK_NAME = "NVDA"
COMPANY_NAME = "NVIDIA Corp"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("OWN_STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("OWN_NEWS_API_KEY")

TWILIO_SID = os.environ.get("OWN_TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("OWN_TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_request = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_request.raise_for_status()
stock_data = stock_request.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

up_down = None

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if difference < 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = (difference / float(day_before_yesterday_closing_price)) * 100

if abs(diff_percentage) > 2:

    news_params = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "language": "en",
    }

    news_request = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_request.raise_for_status()
    articles = news_request.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down} {diff_percentage}% \nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            from_=os.environ.get("OWN_TWILIO_PHONE_NUMBER"),
            body=article,
            to=os.environ.get("OWN_PHONE_NUMBER")
        )
