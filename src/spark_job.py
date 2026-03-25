from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LogProcessor").getOrCreate()

df = spark.read.json("data/logs.json")

df_clean = df.select("status_code", "response_time")

df_clean.write.mode("overwrite").parquet("data/processed")

print("Data processed successfully")
