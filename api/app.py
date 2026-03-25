from fastapi import FastAPI
import mlflow.sklearn

app = FastAPI()

model = mlflow.sklearn.load_model("runs:/f0ea092371b74f63904d7f12643eb2fa/failure-model")

@app.get("/predict")
def predict(response_time: float):
    pred = model.predict([[response_time]])
    return {"failure": int(pred[0])}
