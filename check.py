import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
print("PySpark version:", pyspark.__version__)
spark.stop()