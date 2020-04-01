# Imports
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, array
import pandas as pd

from pyspark.sql.types import StructType, StructField, StringType

import pymongo_spark
pymongo_spark.activate()

MONGODB_URI = "mongodb://heroku_kvptfcm8:vbekldoic9poi92kkp810rvk7@ds141185.mlab.com:41185/heroku_kvptfcm8"


# Define your schema explicitly
schema = StructType([StructField("timestamp", StringType()),
                     StructField("symbol", StringType()),
                     StructField("sentiment", StringType()),
                     StructField("body", StringType())])

def summarize(doc):
    return {"timestamp": str(doc["created_at"]), 
            "symbol": str(doc["symbols"]["symbol"]), 
            "sentiment": str(doc["entities"]["sentiment"]),
            "body": str(doc["body"])}

if __name__ == '__main__':

    # Start spark session
    spark = SparkSession.builder.getOrCreate()
    json_rdd = sc.mongoRDD(MONGODB_URI)

    projected_rdd = data_rdd.map(summarize)
	train_df = sqlcontext.jsonRDD(projected_rdd, schema)
	train_df.first()

    # Stop spark session 
    spark.stop()

