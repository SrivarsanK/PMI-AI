# Phase 03: Deep Learning & RUL Estimation - Discussion Log

**Date:** 2026-03-23
**Mode:** Auto (YOLO)

## Area: Deep Learning Framework
- **Q:** TensorFlow or PyTorch for RUL estimation?
- **Selection:** PyTorch. [auto-selected recommended default]

## Area: Model Architecture
- **Q:** Which RNN variant will be used for time-series memory?
- **Selection:** LSTM. [auto-selected recommended default]

## Area: Inference Performance
- **Q:** How will CPU-heavy DL inference be handled in an async web server?
- **Selection:** ThreadPoolExecutor to prevent blocking. [auto-selected recommended default]

## Area: RUL Strategy
- **Q:** Which labeling strategy for RUL?
- **Selection:** Piecewise Linear RUL. [auto-selected recommended default]
