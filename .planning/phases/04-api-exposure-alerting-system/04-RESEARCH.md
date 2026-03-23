# Phase 04: API Exposure & Alerting System - Research

## Objective
Research real-time alert broadcasting via WebSockets and REST API design for machine health dashboards using FastAPI.

## Findings

### 1. Real-time Alerts (WebSockets)
- **Mechanism**: Use FastAPI `WebSocket` endpoints for low-latency, bi-directional communication.
- **Broadcasting**: Implement a `ConnectionManager` to keep track of active WebSocket clients and broadcast messages to all (or specific groups) when an anomaly or critical RUL is detected.
- **Security**: WebSocket handshakes should be protected via JWT or existing API keys passed as query parameters (since headers are limited in the browser WebSocket API).

### 2. Machine Health REST API
- **Endpoints**:
    - `GET /machines`: List all machines and their current aggregate health status.
    - `GET /machines/{id}/health`: Detailed time-series view including filtered telemetry, anomaly status, and RUL trends.
- **Pydantic**: Use Pydantic models for response serialization to ensure consistent dashboard data.

### 3. Alerting Logic
- **Thresholds**:
    - **Anomaly**: Immediate WebSocket broadcast when the Isolation Forest flags a point.
    - **RUL**: Tiered alerts (e.g., Warning: RUL < 50, Critical: RUL < 20).
- **History**: Store alerts in a lightweight persistent store (or a new InfluxDB bucket) for historical auditing.

### 4. Integration with Frontend
- **Format**: JSON over WebSockets for structured alert packets (type, machine_id, severity, timestamp, description).

## Implementation Path
1. Implement `src/core/connection_manager.py` for WebSocket management.
2. Update `src/api/routes.py` with dashboard GET endpoints.
3. Integrate alert broadcasting into `src/core/tasks.py`.
4. Create `src/api/websockets.py` for the real-time stream.

## Success Criteria for Planning
- Plan 1: WebSocket Connection Manager & Real-time Route.
- Plan 2: Dashboard REST API (Read-only status endpoints).
- Plan 3: Alert Broadcasting (Task -> WebSocket integration).
