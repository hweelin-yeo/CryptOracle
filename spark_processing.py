# Imports
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, array
from pyspark.sql.types import StructType, StructField, StringType

MONGODB_URI = "mongodb://heroku_kvptfcm8:vbekldoic9poi92kkp810rvk7@ds141185.mlab.com:41185/heroku_kvptfcm8"
# TODO: This needs to become the URL of some file system
FILEPATH = "data/gemini_BTCUSD_1hr.csv"

# Define your schema explicitly
schema = StructType([StructField("timestamp", StringType()),
                     StructField("symbol", StringType()),
                     StructField("sentiment", StringType()),
                     StructField("body", StringType())])

def summarize(doc):
	return (doc["created_at"], 
            doc["symbols"]["symbol"], 
            doc["entities"]["sentiment"],
            doc["body"])
    # return {"timestamp": str(doc["created_at"]), 
    #         "symbol": str(doc["symbols"]["symbol"]), 
    #         "sentiment": str(doc["entities"]["sentiment"]),
    #         "body": str(doc["body"])}

def combine_prices_and_messages():
    # NOTE: The environment needs to have scala installed for this to work
    spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/cryptoracle.messages") \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:2.4.0') \
    .getOrCreate()

    messages_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
    prices_df = spark.read.format('csv').load(FILEPATH, header=True, inferSchema=True)

    print("THIS IS MESSAGES COUNT :%d" % messages_df.count())
    print("THIS IS PRICES COUNT :%d" % prices_df.count())
    spark.stop()

if __name__ == '__main__':

    # Start spark session
    # sparkConf = SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.2.0")
    
    # Option 1:
    # sc = SparkSession.builder.config('spark.mongodb.input.uri', MONGODB_URI).getOrCreate()
    # json_rdd = sc.mongoRDD(MONGODB_URI)

    # OPTION 2:provided by https://groups.google.com/forum/#!topic/mongodb-user/ahKXPwlKyxA:

    # OPTION 3:
    combine_prices_and_messages()

