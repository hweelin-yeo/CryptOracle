# CryptOracle

## Steps
1. Tweets - generate tweets
2. Tweets - clean it up, use spark to extract important information (timestamp, symbol, sentiment, trend in sentiment, tweet)
window is set as +- 1 hour?
4. Historical price data -  (timestamp, symbol, price, volume, trend in price)
5. Cryptospecific feature (timestamp, symbol, hashrate)
6. Combined dataset tuple - (timestamp, symbol, price, volume, trend in price, sentiment, trend in sentiment, tweet, hashrate)
7. Model - think of inputs

## Original resources
- Getting StockTwits data: https://github.com/hamx0r/stocktwits
- Stocktwits: https://api.stocktwits.com/developers/docs/authentication
- Python, Heroku, Flask: https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc

# From this repo
- Navigate to stocktwits
- pip install -r requirements.txt
- python2 api.py

# Applying for twitter
- https://developer.twitter.com/en.html
- About:
Cornell University, CS 5304, Data Science in the Wild. This project is our final Project, with Serge Belongie as the professor. Extracting tweets of cryptocurrencies to use it for sentiment analysis, to predict prices.
- Analysis:
Use Spark; analyze sentiments and predict prices. Feature engineering  would be put in place. Used in tandem with cryptocurrency data that is batched over a period of time to form input features. Prices and cryptocurrency metrics are matched with sentiments using timestamps. Sentiment analysis is performed with a confidence interval

# Reasons for choosing currencies
3/24				3/22.             Avg
BCH: 18 			16			17
BNB: 10			7			-
BSV: 23			22			22.5
BTC: 22			10			16
Doge: 18.                  19			18.5
EOS: 2			0			-
ETH: 11			17			14
LTC: 17			12			14.5
XMR: 3			2			-
XRP: 15			9			12


BSV, Doge, BCH, BTC, ETH, LTC
