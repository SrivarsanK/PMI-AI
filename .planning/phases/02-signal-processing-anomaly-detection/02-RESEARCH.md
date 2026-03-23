# Phase 02: Signal Processing & Anomaly Detection - Research

## Objective
Research the implementation of real-time signal processing and unsupervised anomaly detection for industrial sensor data.

## Findings

### 1. Signal Processing (SciPy)
- **Low-pass Filter**: Use a Butterworth filter (`scipy.signal.butter`) to remove high-frequency noise from sensor telemetry.
- **Implementation**: Use Second-Order Sections (`sos`) format for improved numerical stability.
- **Requirement**: Needs a sampling frequency (`fs`) estimate. For Phase 2, we will assume a configurable `fs` or derive it from timestamp deltas.

### 2. Anomaly Detection (Isolation Forest)
- **Choice**: **Isolation Forest** (Scikit-learn) is the preferred algorithm for unsupervised anomaly detection in 2025.
- **Rationale**: Industrial anomalies are rare (data scarcity), and Isolation Forest handles high-dimensional, unlabeled time-series data efficiently.
- **Workflow**:
    1. Collect a baseline window of "normal" data.
    2. Train/Update the Isolation Forest model.
    3. Predict anomaly scores for incoming feature vectors.

### 3. Feature Engineering
- **Rolling Windows**: High-frequency raw values are noisy. Features like **Rolling Mean**, **Standard Deviation**, and **RMS** provide a more stable signal for the model.
- **Window Size**: Start with a window of 50 samples for real-time responsiveness.

### 4. Real-time Architecture
- **FastAPI BackgroundTasks**: After data is stored in InfluxDB, trigger a background task to process the window and update the anomaly status.
- **State Management**: Use an in-memory or Redis-based cache for the last N samples per machine to avoid repeated DB queries for every point.

## Implementation Path
1. Add `scipy` and `scikit-learn` to `requirements.txt`.
2. Implement `src/services/processing_service.py` for SciPy filtering.
3. Implement `src/services/anomaly_service.py` for Isolation Forest logic.
4. Integrate processing into the `/ingest` flow.

## Success Criteria for Planning
- Plan 1: Signal Processing Module (SciPy filters).
- Plan 2: Feature Extraction & Anomaly Model (Isolation Forest).
- Plan 3: Pipeline Integration (Background tasks + Real-time alerting).
