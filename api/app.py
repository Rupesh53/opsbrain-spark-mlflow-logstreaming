from fastapi import FastAPI
import mlflow.sklearn

app = FastAPI()

model = mlflow.sklearn.load_model("runs:/<RUN_ID>/failure-model")

@app.get("/predict")
def predict(response_time: float):
    pred = model.predict([[response_time]])
    return {"failure": int(pred[0])}
