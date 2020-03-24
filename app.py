import logging as log
from requestors import ST_BASE_PARAMS, ST_BASE_URL
import json
import os.path
from datetime import datetime

from urllib.parse import urlparse
from pymongo import MongoClient
# Select which library to use for handling HTTP request.  If running on Google App Engine, use `GAE`.
# Otherwise, use `Requests` which is based on the `requests` module.
from requestors import Requests as R
from flask import Flask

# Example list of exchanges to limit a watchlist to
EXCHANGES = ['NYSE', 'NASDAQ', 'NYSEMkt', 'NYSEArca']
SYMBOLS = ['BTC.X', 'BSV.X', 'BNB.X', 'BCH.X',
           'DOGE.X', 'EOS.X', 'XMR.X', 'XRP.X',
           'ETH.X', 'LTC.X']
SYMBOLS_FINAL = ['EOS.X', 'DOGE.X', 'BTC.X',
               'ETH.X', 'LTC.X']

# ---------------------------------------------------------------------
# Mongo setup
# https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
# ---------------------------------------------------------------------

MONGO_URL = os.environ.get('MONGODB_URI')
if not MONGO_URL:
  MONGO_URL = "mongodb://heroku_kvptfcm8:vbekldoic9poi92kkp810rvk7@ds141185.mlab.com:41185/heroku_kvptfcm8"

db_name = urlparse(MONGO_URL).path[1:]
client = MongoClient(MONGO_URL)
db = client[db_name]

app = Flask(__name__)

@app.route("/")
def getRuns():
  res = db.runs.count()
  print(res)
  return res

# ---------------------------------------------------------------------
# Cronjob setup
# ---------------------------------------------------------------------

def cronjob():
  print("Cron job is running")
  for symbol in SYMBOLS:
    dt_string = datetime.now().strftime("%d-%m-%H:%M")
    print(without_token_get_stock_stream(symbol, "json/compiled_" + symbol + dt_string + ".json"))

# ---------------------------------------------------------------------
# StockTwits
# ---------------------------------------------------------------------
def without_token_get_stock_stream(symbol, output_filename, params={}):
  """ gets stream of messages for given symbol"""
  result = R.get_json(ST_BASE_URL + 'streams/symbol/{}.json'.format(symbol))
  
  print(result)
#  if os.path.isfile(output_filename):
#    f = open(output_filename, "a+")
#  else:
#    f = open(output_filename, "w")
#
#  f.write(json.dumps(result))
#  f.close()

  runs = db.runs
  run_result = runs.insert_one(result)
  print('One run: {0}'.format(run_result.inserted_id))
  return result

def get_stock_stream(symbol, output_filename, params={}):
    """ gets stream of messages for given symbol
    """
    print("printing stock stream")
    all_params = ST_BASE_PARAMS.copy()
    for k, v in params.items():
        all_params[k] = v
    result = R.get_json(ST_BASE_URL + 'streams/symbol/{}.json'.format(symbol), params=all_params)


    if os.path.isfile(output_filename):
      f = open(output_filename, "a+")
    else:
      f = open(output_filename, "w")

    #    result = R.get_json(ST_BASE_URL + 'streams/symbol/{}.json'.format(symbol))
    f.write(json.dumps(result))

    return result

if __name__ == '__main__':
  app.run()
