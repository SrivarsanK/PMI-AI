# ARCHITECTURE.md — PMI-AI System Architecture

## System Structure for Time-Series Predictive Maintenance

The **PMI-AI** system is structured as a multi-layered data pipeline designed for high-volume sensor telemetry and low-latency prediction.

### 1. Data Ingestion & Acquisition
- **IoT Sensors & Gateways**: Sensors (vibration, temperature, pressure) transmit data via Industrial Gateways.
- **Data Ingestion Layer**: Scalable ingestion via FastAPI endpoints or MQTT brokers for real-time telemetry.

### 2. Processing & Transformation
- **Data Preprocessing Pipeline**: Cleaning, normalization, and handling of missing or noisy sensor data.
- **Feature Engineering**: Rolling window calculations, statistical aggregates, and frequency-domain features (FFT for vibration analysis).
- **Time-Series Handling**: Managing chronological order, trend/seasonality, and clock drift.

### 3. Machine Learning & Analytics Layer
- **Model Inference Engine**: Served via FastAPI to provide real-time RUL estimation and failure probability.
- **Training Pipeline (MLOps)**: Automated retraining based on new maintenance outcomes using MLflow or DVC.
- **Deep Learning Layer**: RNN/LSTM/GRU for temporal dependencies and Grad-CAM or LIME for model explainability (XAI).

### 4. Storage Layer
- **InfluxDB (Primary TSDB)**: For high-speed sensor reading storage and windowing queries.
- **PostgreSQL**: For metadata, user profiles, alert history, and system configuration.

### 5. Deployment & Infrastructure
- **API (FastAPI)**: Serves internal and external applications with prediction data.
- **Grafana (Monitoring)**: For real-time monitoring of dashboard metrics and system health.
- **Containerization (Docker)**: Ensuring consistent environments across development and industrial deployment.

### Suggested Build Order
1. **Infrastructure**: Ingestion API & Storage (InfluxDB).
2. **Data Pipeline**: Preprocessing & Feature Engineering modules.
3. **Core AI Models**: Initial Random Forest/LSTM for failure probability.
4. **Advanced AI**: RUL Estimation and XAI (Explainable AI).
5. **Dashboard & API**: Frontend exposure and alerting system.

---
*Generated: 2026-03-23*
