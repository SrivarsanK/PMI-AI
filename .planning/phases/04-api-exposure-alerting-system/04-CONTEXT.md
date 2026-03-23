# Phase 04: API Exposure & Alerting System - Context

**Gathered:** 2026-03-23
**Status:** Ready for planning

<domain>
## Phase Boundary

Expose machine health metadata, anomaly status, and RUL estimates via RESTful and WebSocket APIs for consumption by a real-time dashboard or monitoring personnel.
</domain>

<decisions>
## Implementation Decisions

### Communication
- **D-01:** Real-time Transport: **WebSockets**. Used to broadcast critical alerts immediately as they are detected in background tasks.
- **D-02:** Data Exposure: **REST API**. Traditional HTTP GET endpoints for dashboard initialization and historical health status retrieval.

### Security
- **D-03:** WebSocket Authentication: API Key as a **Query Parameter** (`?api_key=...`) to bypass the header limitations of some WebSocket clients.

### API Structure
- **D-04:** Healthy vs. Critical: Machines will be categorized by health status:
    - **Healthy**: No anomalies, RUL > 50.
    - **Warning**: RUL between 20 and 50.
    - **Critical**: Active anomaly OR RUL < 20.
</decisions>

<canonical_refs>
## Canonical References

### Project & Research
- `.planning/PROJECT.md`
- `.planning/research/STACK.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/SUMMARY.md`
- `.planning/phases/04-api-exposure-alerting-system/04-RESEARCH.md`
</canonical_refs>

<deferred>
## Deferred Ideas
- **D-05:** Email/SMS Alerts: Deferred until Phase 6 (if requested by user). Initial Phase 4 focus is only on the API/Websocket layer for the internal dashboard.
- **D-06:** Role-Based Access Control (RBAC): Deferred until v2.0.
</deferred>
