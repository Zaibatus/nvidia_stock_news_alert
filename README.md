# NVIDIA Stock Price Alert System

**Description**

This project is a Python-based application that sends an SMS alert when the NVIDIA Corp (NVDA) stock price increases or decreases by 5% or more, compared to the previous day's closing price. The SMS includes the percentage change in the stock price and the first three news articles related to NVIDIA Corp, with their titles and descriptions.

**APIs Used**

- Twilio API: For sending SMS alerts.
- Alpha Vantage API: For retrieving stock price data.
- News API: For fetching the latest news articles related to NVIDIA Corp.

**How It Works**

1) Fetch the daily stock prices for NVIDIA Corp from Alpha Vantage.
2) Calculate the percentage difference between the closing prices of the last two days.
3) If the percentage difference is 5% or more (increase or decrease), fetch the latest news articles about NVIDIA Corp from News API.
4) Send an SMS using Twilio, including the percentage change in the stock price and the first three news articles with their titles and descriptions.
