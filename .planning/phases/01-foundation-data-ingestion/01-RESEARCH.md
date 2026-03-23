# Phase 01: Foundation & Data Ingestion - Research

## Objective
Research the technical foundation for high-frequency telemetry ingestion using FastAPI and InfluxDB 2.x for the PMI-AI system.

## Findings

### 1. Ingestion Strategy (FastAPI)
- **Asynchronous Handlers**: Use `async def` for all telemetry ingestion endpoints to maximize throughput without blocking on I/O.
- **Background Tasks**: Offload heavy processing (e.g., historical aggregation or complex validation) to FastAPI `BackgroundTasks`.
- **Batching**: While individual sensors may POST single readings, the backend should aggregate these into batches before writing to InfluxDB. The optimal batch size for InfluxDB is ~5000 lines.
- **Pydantic v2**: Leverage Pydantic for strict schema validation. Dropping malformed data at the edge ensures the ML pipeline receives clean data.

### 2. Time-Series Storage (InfluxDB 2.x)
- **Schema Design**: 
    - **Measurement**: `telemetry`
    - **Tags**: `machine_id`, `sensor_type` (high-speed indexing).
    - **Fields**: `value` (float).
- **Precision**: Use millisecond or second precision unless microsecond is strictly required to save storage/index overhead.
- **Client**: Use `influxdb-client[async]` for non-blocking writes.

### 3. Authentication
- **Security Scheme**: `APIKeyHeader` (using `X-API-Key`) via FastAPI's `Security` dependencies.
- **Benefit**: Native support in FastAPI's `/docs` (OpenAPI) and simple implementation for industrial hardware.

### 4. Deployment Pattern
- **ASGI**: Uvicorn with Gunicorn workers.
- **Instrumentation**: OpenTelemetry for tracing high-frequency request performance.

## Implementation Path
1. Initialize FastAPI application with dependency injection for InfluxDB and API Key.
2. Define Pydantic models for `telemetry` payload.
3. Implement `InfluxDBService` with asynchronous batch writing.
4. Create the ingestion endpoint with strict validation.

## Success Criteria for Planning
- Plan 1: Backend Setup (FastAPI + Pydantic + Security).
- Plan 2: Data Service (InfluxDB integration + Batching logic).
- Plan 3: Ingestion API (Endpoints + Documentation).
