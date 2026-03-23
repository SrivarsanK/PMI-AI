# STACK.md — PMI-AI Tech Stack

## Recommended 2025 Stack for Predictive Maintenance

Based on current industry standards and the project's specific requirements, here is the recommended technical stack.

### 1. Core Language & Backend
- **Python 3.12+**: The de-facto standard for AI/ML development.
- **FastAPI**: High-performance, asynchronous web framework for serving predictions.
- **Pydantic v2**: For robust data validation and settings management.

### 2. Machine Learning & Deep Learning
- **PyTorch 2.x**: Preferred for its dynamic computation graph and extensive research community support for LSTM/GRU.
- **TensorFlow/Keras**: Strong alternative, particularly for production deployment via TFX.
- **Scikit-learn**: For traditional ML models (Random Forest, Gradient Boosting) and preprocessing.

### 3. Time-Series Analysis & Signal Processing
- **NumPy & SciPy**: Fundamental libraries for numerical computing and advanced signal processing (FFT, filtering).
- **Pandas**: Efficient manipulation and analysis of structured time-series data.
- **Statsmodels**: For statistical time-series modeling (ARIMA, etc.) if needed.

### 4. Data Storage & Pipelines
- **InfluxDB**: High-performance Time-Series Database (TSDB) for storing sensor telemetry.
- **PostgreSQL (with TimescaleDB extension)**: More versatile alternative if relational data is also prominent.
- **Apache Kafka / Faust**: For high-volume stream processing if scaling to hundreds of machines.

### 5. API Best Practices (FastAPI)
- **Dependency Injection**: Use for database sessions and model loading.
- **Asynchronous Operations**: Maximize concurrency for I/O-bound sensor ingestion.
- **Gunicorn with Uvicorn workers**: Recommended for production deployment.

### What NOT to Use
- **Flask**: Lower performance compared to FastAPI for high-concurrency sensor data.
- **Traditional RDBMS (without TSDB extensions)**: Will struggle with the high-speed ingestion and storage of raw time-series sensor data.

---
*Generated: 2026-03-23*
