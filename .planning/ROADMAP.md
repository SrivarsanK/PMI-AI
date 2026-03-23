# Roadmap: PMI-AI

## Overview

The journey of **PMI-AI** starts with building a robust time-series data foundation, moving through signal processing to clear the industrial noise, and culminating in high-precision deep learning models for failure prediction and Remaining Useful Life (RUL) estimation. We'll deliver a production-ready API that enables proactive maintenance for industrial sensors.

## Phases

- [ ] **Phase 1: Foundation & Data Ingestion** - Establish FastAPI server, InfluxDB storage, and real-time sensor ingestion API.
- [ ] **Phase 2: Signal Processing & Anomaly Detection** - Implement SciPy-based noise filtering and initial machine learning for anomaly detection.
- [ ] **Phase 3: Deep Learning & RUL Estimation** - Integrate LSTM/GRU models to predict Remaining Useful Life (RUL) from temporal sequences.
- [ ] **Phase 4: API Exposure & Alerting System** - Finalize the predictive API, alerting logic, and documentation for industrial integration.

## Phase Details

### Phase 1: Foundation & Data Ingestion
**Goal**: Establish a scalable backend capable of receiving and storing high-frequency sensor telemetry.
**Depends on**: Nothing
**Requirements**: REQ-01 (Sensor Monitoring), REQ-05 (API Layer)
**Success Criteria**:
  1. FastAPI server is running and accepting sensor payloads (Temperature, Vibration, Pressure).
  2. Data is successfully persisted to InfluxDB with correct timestamps.
  3. API documentation (Swagger) is available and functional.
**Plans**: 3 plans

Plans:
- [ ] 01-01: Backend Skeleton (FastAPI + Project Structure).
- [ ] 01-02: Data Layer (InfluxDB Integration + Schemas).
- [ ] 01-03: Ingestion API (Telemetry Endpoints + Validation).

### Phase 2: Signal Processing & Anomaly Detection
**Goal**: Clean noisy industrial data and implement the first layer of failure intelligence.
**Depends on**: Phase 1
**Requirements**: REQ-02 (Failure Prediction)
**Success Criteria**:
  1. Signal processing module successfully filters raw sensor noise (FFT/Low-pass).
  2. Statistical features (Mean, STD, Rolling Windows) are computed for telemetry streams.
  3. Initial anomaly detection model (e.g., Random Forest) can flag abnormal machine states.
**Plans**: 2 plans

Plans:
- [ ] 02-01: DSP Module (SciPy/NumPy filters + Feature extraction).
- [ ] 02-02: Anomaly Detection (Model training + Evaluation).

### Phase 3: Deep Learning & RUL Estimation
**Goal**: Leverage the temporal nature of machinery health to predict the exact remaining lifespan.
**Depends on**: Phase 2
**Requirements**: REQ-03 (RUL Estimation)
**Success Criteria**:
  1. LSTM/GRU model is trained and capable of sequence-to-sequence prediction.
  2. The system outputs a numerical RUL (Remaining Useful Life) estimation in hours/days.
  3. Model performance is validated against historical failure sequences.
**Plans**: 2 plans

Plans:
- [ ] 03-01: Deep Learning Engine (PyTorch/TensorFlow sequence models).
- [ ] 03-02: RUL Predictor (Integration of sequence data into RUL outputs).

### Phase 4: API Exposure & Alerting System
**Goal**: Turn predictions into actionable industrial maintenance schedules.
**Depends on**: Phase 3
**Requirements**: REQ-04 (Proactive Scheduling), REQ-05 (API Layer)
**Success Criteria**:
  1. Predicton API returns RUL and failure probability for any given machine ID.
  2. Alerting logic triggers proactive maintenance events based on configurable thresholds.
  3. Complete integration of the "predictive" loop from sensor ingest to proactive alert.
**Plans**: 2 plans

Plans:
- [ ] 04-01: Prediction API (Endpoints for RUL & Probability).
- [ ] 04-02: Alerting & Scheduling (Proactive logic + Final integration).

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation & Ingestion | 0/3 | Not started | - |
| 2. Processing & Anomaly | 0/2 | Not started | - |
| 3. Deep Learning & RUL | 0/2 | Not started | - |
| 4. API & Alerting | 0/2 | Not started | - |

---
*Last updated: 2026-03-23 after initialization*
