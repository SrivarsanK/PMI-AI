# Phase 05: Maintenance Management & Automated Analytics - Context

**Gathered:** 2026-03-23
**Status:** In Planning

<domain>
## Phase Boundary

Advance from raw RUL/Anomaly detection into a "Actionable Maintenance Schedule" that ranks and organizes maintenance events based on industrial-grade prioritization (RIME-like). 
</domain>

<decisions>
## Implementation Decisions

### Maintenance Sorting
- **D-01:** Primary Sorting: **Remaining Useful Life (RUL)**. Machines with lowest RUL are ranked first.
- **D-02:** Secondary Sorting: **Anomaly Frequency**. If RUL is equal, prioritize machines with more recent anomalies.

### Maintenance Actions
- **D-03:** Maintenance Thresholds:
    - **EMERGENCY**: RUL < 10. (Needs immediate attention, < 1 day roughly).
    - **URGENT**: RUL < 20. (Scheduled within 2 days).
    - **RECOMMENDED**: RUL < 50. (Scheduled within the week).
</decisions>

<canonical_refs>
## Canonical References

### Project & Research
- `.planning/PROJECT.md`
- `.planning/phases/05-maintenance-management-automated-analytics/05-RESEARCH.md`
</canonical_refs>

<deferred>
## Deferred Ideas
- **D-04:** Logistics Integration: (Ordering parts or scheduling third-party technicians). Deferred until Phase 7.
- **D-05:** Full Inventory Sync for spare parts used in maintenance.
</deferred>
