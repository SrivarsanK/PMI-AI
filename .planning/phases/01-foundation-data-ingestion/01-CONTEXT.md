# Phase 01: Foundation & Data Ingestion - Context

**Gathered:** 2026-03-23
**Status:** Ready for planning

<domain>
## Phase Boundary

Establish a scalable backend capable of receiving and storing high-frequency sensor telemetry. Focus on core infrastructure: FastAPI server, InfluxDB storage, and the ingestion API.
</domain>

<decisions>
## Implementation Decisions

### API Ingestion
- **D-01:** API Ingestion Format: **JSON**. Selected for ease of validation and integration.
- **D-02:** Data Validation: **Strict Pydantic**. Malformed readings will be dropped to ensure data quality.

### Data Storage & Schema
- **D-03:** Database Selection: **InfluxDB**. Primary storage for all time-series telemetry.
- **D-04:** Schema Design: **Tagged Storage**. Data tagged by `machine_id` and `sensor_type` for high-speed RUL queries.

### Security
- **D-05:** Sensor Authentication: **API Keys**. Gateways will authenticate via `X-API-Key` header.
</decisions>

<canonical_refs>
## Canonical References

### Project & Research
- `.planning/PROJECT.md`
- `.planning/research/STACK.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/SUMMARY.md`
</canonical_refs>

<deferred>
## Deferred Ideas
- **D-06:** MessagePack Support: Revisit if JSON performance becomes a bottleneck.
</deferred>
