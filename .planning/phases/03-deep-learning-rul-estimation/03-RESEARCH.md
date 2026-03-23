# Phase 03: Deep Learning & RUL Estimation - Research

## Objective
Research the implementation of Remaining Useful Life (RUL) estimation using Deep Learning (LSTM) in a real-time FastAPI environment.

## Findings

### 1. Model Architecture (LSTM)
- **Choice**: **LSTM (Long Short-Term Memory)**.
- **Rationale**: LSTMs are specifically designed to handle sequential data and can "remember" early degradation signs that simple regression models miss.
- **Structure**: Input layer (normalized sensor window) -> LSTM hidden layers -> Fully Connected (Dense) layer -> Single output (RUL value).
- **Labeling**: Use a **Piecewise Linear RUL** strategy (constant RUL during the early "healthy" phase, followed by a linear decrease to zero at failure).

### 2. Deep Learning Framework (PyTorch)
- **Framework**: **PyTorch**.
- **Optimization**: Use `torch.jit` (TorchScript) for production-grade inference speed. 
- **Quantization**: Apply dynamic quantization (`torch.quantization.quantize_dynamic`) to reduce CPU latency if needed.

### 3. Inference Strategy
- **Offloading**: Since deep learning inference is CPU-heavy, it should be run in a `ThreadPoolExecutor` within the FastAPI background task to prevent blocking the async event loop (GIL management).
- **Batching**: While real-time inference is point-by-point, if multiple machines are ingested simultaneously, dynamic batching can significantly improve throughput.

### 4. Data Preparation
- **Fixed Window Size**: The LSTM requires a fixed-length historical sequence (e.g., last 30 readings).
- **Normalization**: Sensors must be scaled (Min-Max or Z-score) based on historical training data distribution.

## Implementation Path
1. Add `torch` and `torchvision` (if needed) to `requirements.txt`.
2. Implement `src/services/deep_learning_service.py` for RUL prediction.
3. Define the LSTM model class in `src/models/lstm.py`.
4. Integrate RUL estimation into the `process_telemetry_task` in `src/core/tasks.py`.

## Success Criteria for Planning
- Plan 1: LSTM Model Definition & Weight Loading.
- Plan 2: Deep Learning Service (Inference logic).
- Plan 3: Pipeline Integration (RUL estimation in background).
