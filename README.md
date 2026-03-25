# 🚀 OpsBrain: Real-Time MLOps Pipeline with Spark Streaming & MLflow

## 📌 Overview

OpsBrain is a **real-time DevOps intelligence system** that processes live logs using **Apache Spark Structured Streaming** and predicts system failures using a machine learning model tracked in **MLflow**.

This project demonstrates a **local MLOps setup** similar to modern data platforms, enabling:

* Continuous log ingestion
* Real-time data processing
* Model training & tracking
* Live prediction via API and streaming

---

## 🏗️ Architecture

```
Log Producer → Spark Streaming → Processed Data → MLflow Model
        ↓                               ↓
     Raw Logs                    Stream Predictions
        ↓                               ↓
     Storage                     FastAPI (On-demand API)
```

---

## ⚙️ Tech Stack

* **Streaming Engine**: Apache Spark (Structured Streaming)
* **ML Lifecycle**: MLflow
* **API Layer**: FastAPI
* **Containerization**: Docker & Docker Compose
* **Language**: Python

---

## 📂 Project Structure

```
opsbrain-spark-mlflow/

├── api/
│   └── app.py                 # FastAPI app for predictions
├── src/
│   ├── log_producer.py        # Generates real-time logs
│   ├── stream_job.py          # Spark streaming ETL
│   ├── stream_predict.py      # Real-time predictions
│   └── train.py               # Model training script
├── data/
│   ├── stream/                # Raw logs
│   ├── stream_processed/      # Processed parquet data
│   └── checkpoints/           # Spark checkpoints
├── Dockerfile.api
├── Dockerfile.spark
├── Dockerfile.mlflow
├── docker-compose.yml
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Build the project

```bash
docker-compose build
```

---

### 2️⃣ Start streaming pipeline

```bash
docker-compose up log-producer spark-stream
```

⏳ Wait 30–60 seconds for data generation

---

### 3️⃣ Verify data generation

```bash
ls data/
```

Expected:

```
stream/
stream_processed/
checkpoints/
```

---

### 4️⃣ Train the model

```bash
docker-compose run mlflow python src/train.py
```

---

### 5️⃣ Open MLflow UI

```
http://localhost:5000
```

* Go to experiment
* Click a run
* Copy **RUN_ID**

---

### 6️⃣ Update model reference

Update in:

#### `api/app.py`

#### `src/stream_predict.py`

```python
model = mlflow.pyfunc.load_model("runs:/<RUN_ID>/failure-model")
```

---

### 7️⃣ Start full system

```bash
docker-compose up
```

---

## 🧪 Testing

---

### ✅ Test API (On-demand prediction)

Open:

```
http://localhost:8000/predict?response_time=900
```

Example response:

```json
{"failure": 1}
```

---

### ✅ Test Streaming Predictions

```bash
docker-compose logs -f spark-predict
```

Expected:

```
Predictions:
response_time=1200 → failure=1
response_time=100 → failure=0
```

---

### ✅ Swagger UI

```
http://localhost:8000/docs
```

---

## 🔄 Data Flow

```
log_producer.py
   ↓
Spark Streaming (stream_job.py)
   ↓
Parquet Data (data/stream_processed)
   ↓
Model Training (train.py)
   ↓
MLflow Model Registry
   ↓
Predictions:
   → API (app.py)
   → Streaming (stream_predict.py)
```

---

## 💡 Key Features

* Real-time log ingestion
* Streaming ETL pipeline
* ML model tracking with MLflow
* Batch + streaming hybrid architecture
* REST API for inference
* Fully containerized setup

---

## 🧠 Use Cases

* DevOps failure prediction
* System performance monitoring
* Anomaly detection in logs
* Real-time alerting systems

---

## 🚨 Troubleshooting

### ❌ MLflow UI not opening

* Check container logs:

```bash
docker-compose logs mlflow
```

---

### ❌ No data in `stream_processed`

* Ensure streaming is running:

```bash
docker-compose logs spark-stream
```

---

### ❌ Model not loading

* Verify RUN_ID is correct

---

### ❌ API not responding

```bash
docker-compose restart api
```

---

## 💬 Resume / LinkedIn Highlight

> Built a real-time MLOps pipeline using Apache Spark Structured Streaming and MLflow, enabling continuous log processing and failure prediction via API and streaming.

---

## 🚀 Future Enhancements

* Integrate Apache Kafka for real streaming
* Add Grafana dashboard for visualization
* Deploy on Kubernetes (AKS)
* Implement auto model retraining
* Add alerting (Slack/Email)

---

## 👨‍💻 Author

Rupesh Nayak

---

## ⭐ If you like this project

Give it a star ⭐ and share on LinkedIn!
