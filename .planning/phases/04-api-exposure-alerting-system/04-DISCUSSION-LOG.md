# Phase 04: API Exposure & Alerting System - Discussion Log

**Date:** 2026-03-23
**Mode:** Auto (YOLO)

## Area: Real-time Transport
- **Q:** How to push alerts to the dashboard?
- **Selection:** WebSockets. [auto-selected recommended default]

## Area: API Security
- **Q:** How to secure WebSocket handshake?
- **Selection:** Token as Query Param. [auto-selected recommended default]

## Area: Health Categorization
- **Q:** Thresholds for Machine Health levels?
- **Selection:** Healthy (>50 RUL), Warning (20-50 RUL), Critical (<20 RUL). [auto-selected recommended default]

## Area: Task Integration
- **Q:** When to broadcast?
- **Selection:** Direct broadcast from the background task if anomaly/critical RUL is detected. [auto-selected recommended default]
