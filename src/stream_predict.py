from pyspark.sql import SparkSession
import mlflow.pyfunc

spark = SparkSession.builder.appName("Predict").getOrCreate()

model = mlflow.pyfunc.load_model("runs:/<RUN_ID>/failure-model")

df = spark.readStream.format("parquet").load("data/stream_processed")

def predict_batch(batch_df, epoch_id):
    pdf = batch_df.toPandas()
    if len(pdf) > 0:
        preds = model.predict(pdf[["response_time"]])
        pdf["prediction"] = preds
        print(pdf)

query = df.writeStream.foreachBatch(predict_batch).start()
query.awaitTermination()
