# CryptOracle

## Steps
1. Tweets - generate tweets
2. Tweets - clean it up, use spark to extract important information (timestamp, symbol, sentiment, trend in sentiment, tweet)
window is set as +- 1 hour?
4. Historical price data -  (timestamp, symbol, price, volume, trend in price)
5. Cryptospecific feature (timestamp, symbol, hashrate)
4. Combined dataset tuple - (timestamp, symbol, price, volume, trend in price, sentiment, trend in sentiment, tweet, hashrate)

## Original resources
- Getting StockTwits data: https://github.com/hamx0r/stocktwits
- Stocktwits: https://api.stocktwits.com/developers/docs/authentication

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

