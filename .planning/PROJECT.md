# PMI-AI: Predictive Maintenance Intelligence System

## What This Is

PMI-AI is an AI-based industrial automation system designed to predict equipment failures and optimize maintenance schedules. By treating machinery health as a time-series prediction problem, the system monitors sensor data (vibration, temperature, pressure) to learn normal operating patterns and estimate the Remaining Useful Life (RUL) of industrial assets.

## Core Value

Predict machine failures in advance to enable proactive maintenance, reducing unplanned downtime and high maintenance costs.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] **[REQ-01] Continuous Sensor Monitoring**: Ingest and process real-time data from temperature, vibration, and pressure sensors.
- [ ] **[REQ-02] Failure Prediction**: Implement time-series analysis to predict potential equipment failures before they occur.
- [ ] **[REQ-03] RUL Estimation**: Estimate the Remaining Useful Life (RUL) of machinery based on historical and real-time data.
- [ ] **[REQ-04] Proactive Scheduling**: Provide actionable maintenance schedules based on AI predictions rather than fixed intervals.
- [ ] **[REQ-05] API Layer**: Build a robust Backend/API using FastAPI to serve predictions and handle data flow.

### Out of Scope

- [ ] **Hardware Sensor Manufacturing**: We focus on the software/AI intelligence layer, not the physical sensor hardware.
- [ ] **Legacy Manual Logs**: The system prioritizes digital sensor data over manual paper-based maintenance logs.

## Context

Industries currently face significant financial losses due to unplanned machine failures and inefficient preventive maintenance (servicing machines when not needed). Existing manual monitoring is slow and error-prone. PMI-AI aims to solve these by applying modern deep learning (LSTM/GRU) and machine learning (Random Forest, Gradient Boosting) techniques to sensor telemetry.

## Constraints

- **Tech Stack**: Python, FastAPI, TensorFlow/PyTorch, NumPy, SciPy.
- **Data Type**: Time-series sensor readings, vibration/temperature logs, and historical failure data.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| AI as Time-Series Problem | Machinery health is best captured as sequential sensor data over time. | — Pending |
| FastAPI for Backend | Fastest growing and most performant Python web framework for ML APIs. | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd:transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-03-23 after initialization*
