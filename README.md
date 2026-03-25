# DevOps MLOps Spark Streaming Project

## Run Steps

1. Install deps:
pip install -r requirements.txt

2. Batch:
python src/spark_job.py
python src/train.py
mlflow ui

3. Streaming:
python src/stream_job.py
python src/log_producer.py
python src/stream_predict.py

4. API:
uvicorn api.app:app --reload
