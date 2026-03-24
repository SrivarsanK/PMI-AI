# Requirements: PMI-AI

## Active
- [x] **[REQ-01] Continuous Sensor Monitoring**: Ingest and process real-time data from temperature, vibration, and pressure sensors. (Validated Phase 1)
- [x] **[REQ-02] Failure Prediction**: Implement time-series analysis to predict potential equipment failures before they occur. (Validated Phase 2)
- [x] **[xEQ-03] RUL Estimation**: Estimate the Remaining Useful Life (RUL) of machinery based on historical and real-time data. (Validated Phase 3)
- [x] **[REQ-04] Proactive Scheduling**: Provide actionable maintenance schedules based on AI predictions rather than fixed intervals. (Validated Phase 4 - Alerts Implementation)
- [x] **[REQ-05] API Layer**: Build a robust Backend/API using FastAPI to serve predictions and handle data flow. (Validated Phase 1..4)

## New (Proposed)
- [ ] **[REQ-06] Maintenance Ranking**: Priority-based list of machines requiring attention sorted by RUL/Risk.
- [ ] **[REQ-07] Historical Maintenance Audit**: Tracking actual vs predicted failure events to improve model confidence.
