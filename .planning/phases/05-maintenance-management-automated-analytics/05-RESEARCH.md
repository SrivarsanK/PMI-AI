# Phase 05: Maintenance Management & Automated Analytics - Research

## Objective
Research prioritization algorithms and scheduling logic to transform RUL predictions into actionable industrial maintenance plans.

## Findings

### 1. Prioritization (Ranking)
- **RIME (Ranking Index for Maintenance Expenditure)**: Use a matrix of Machine Criticality x Failure Urgency (RUL).
- **Urgency Thresholds**:
    - Immediate: RUL < 10
    - Urgent: RUL < 20
    - Routine: RUL < 50
- **Tie-breaking**: Use "Confidence Score" from the LSTM or recent Anomaly counts to break ties between machines with similar RUL.

### 2. Maintenance Scheduling
- **Dynamic Scheduling**: Move away from calendar-based to condition-based.
- **Maintenance Windows**: Group machines in the same production line if one requires "Immediate" maintenance to minimize total downtime.

### 3. MTBF and Reliability Analytics
- **MTBF (Mean Time Between Failures)**: Calculated as Total Up Time / Number of Failures.
- **Reliability Trend**: Tracking the slope of RUL degradation over time to identify "Accelerated Wear" scenarios.

## Implementation Path
1. Create `src/services/maintenance_service.py` for ranking and scheduling logic.
2. Implement `GET /maintenance/schedule` REST endpoint.
3. Add MTBF calculations to the dashboard API.
