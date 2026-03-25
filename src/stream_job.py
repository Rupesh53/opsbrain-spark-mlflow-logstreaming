from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Streaming").getOrCreate()

df = spark.readStream.format("json") \
    .schema("timestamp STRING, status_code INT, response_time INT") \
    .load("data/stream")

df_clean = df.select("status_code", "response_time")

query = df_clean.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "data/stream_processed") \
    .option("checkpointLocation", "data/checkpoints") \
    .start()

query.awaitTermination()
