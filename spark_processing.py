# Imports
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, array
import pandas as pd

import pymongo_spark
pymongo_spark.activate()

from pyspark.sql.types import StructType, StructField, StringType

MONGODB_URI = "mongodb://heroku_kvptfcm8:vbekldoic9poi92kkp810rvk7@ds141185.mlab.com:41185/heroku_kvptfcm8"


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

if __name__ == '__main__':

    # Start spark session
    # sparkConf = SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.2.0")
    sc = SparkSession.builder.config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.11:2.2.0' ).getOrCreate()
    # sc = SparkContext(conf = sparkConf)
    json_rdd = sc.mongoRDD(MONGODB_URI)

    summarize_rdd = data_rdd.map(summarize) # train_df = sqlcontext.jsonRDD(projected_rdd, schema)
    summarize_rdd.first()

    # Stop spark session 
    spark.stop()

