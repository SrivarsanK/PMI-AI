# Phase 02: Signal Processing & Anomaly Detection - Context

**Gathered:** 2026-03-23
**Status:** Ready for planning

<domain>
## Phase Boundary

Implement a robust signal processing pipeline to filter high-frequency industrial sensor noise and a machine-learning-based anomaly detection system using the Isolation Forest algorithm.
</domain>

<decisions>
## Implementation Decisions

### Signal Processing
- **D-01:** Noise Filter: **2nd Order Butterworth Low-pass Filter**. This will be applied to the raw sensor telemetry to remove high-frequency noise from industrial environments.
- **D-02:** Sampling Frequency: Handled as a configurable parameter (`fs`) for each machine/sensor combination.

### Anomaly detection
- **D-03:** Algorithm Selection: **Isolation Forest** (Scikit-learn). An unsupervised approach is required as labeled anomaly data is typically unavailable for industrial setups.
- **D-04:** Detection Features: Models will be trained on the **Rolling Mean** and **Rolling Standard Deviation** of the filtered data (Window size: 50).
- **D-05:** In-Memory Cache: Maintain a temporary buffer of the most recent 100 points per machine in memory (or a simple Python dictionary) for fast rolling window calculation.

### Integration
- **D-06:** Asynchronous Processing: Trigger signal processing and anomaly detection using **FastAPI BackgroundTasks** immediately after storing raw data in InfluxDB.
</decisions>

<canonical_refs>
## Canonical References

### Project & Research
- `.planning/PROJECT.md`
- `.planning/research/STACK.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/SUMMARY.md`
- `.planning/phases/02-signal-processing-anomaly-detection/02-RESEARCH.md`
</canonical_refs>

<deferred>
## Deferred Ideas
- **D-07:** Redis for State Management: Revisit if the in-memory dictionary grows too large with hundreds of sensors.
</deferred>
