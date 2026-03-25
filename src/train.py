import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# df = pd.read_parquet("data/processed")
df = pd.read_parquet("data/stream_processed")
X = df[["response_time"]]
y = (df["status_code"] >= 500).astype(int)

mlflow.start_run()

model = RandomForestClassifier()
model.fit(X, y)

mlflow.sklearn.log_model(model, "failure-model")
mlflow.log_metric("accuracy", model.score(X, y))

mlflow.end_run()

print("Model trained")
