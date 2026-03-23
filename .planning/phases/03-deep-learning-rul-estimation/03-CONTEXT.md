# Phase 03: Deep Learning & RUL Estimation - Context

**Gathered:** 2026-03-23
**Status:** Ready for planning

<domain>
## Phase Boundary

Integrate Deep Learning (LSTM) models into the PMI-AI pipeline to estimate the Remaining Useful Life (RUL) of machinery based on temporal sensor patterns.
</domain>

<decisions>
## Implementation Decisions

### Model Architecture
- **D-01:** Sequence Model: **LSTM (Long Short-Term Memory)**. Ideal for learning degradation over time. 
- **D-02:** Model Framework: **PyTorch**. The model will be exported as a TorchScript (`.pt`) file for fast inference in production.
- **D-03:** Input Strategy: **Sliding Window (Size: 30)**. Predictions require the last 30 normalized sensor values.

### RUL Strategy
- **D-04:** Labeling Convention: **Piecewise Linear RUL**. RUL is assumed constant (threshold: 130) until degradation is detected, then decreases linearly to zero.

### Performance & Scaling
- **D-05:** GIL Mitigation: Run `DeepLearningService.predict` in a **ThreadPoolExecutor** within the FastAPI background task to prevent blocking the asynchronous event loop.
- **D-06:** Model Pre-loading: Load the PyTorch model once during application startup and reuse the instance for all inference requests.
</decisions>

<canonical_refs>
## Canonical References

### Project & Research
- `.planning/PROJECT.md`
- `.planning/research/STACK.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/SUMMARY.md`
- `.planning/phases/03-deep-learning-rul-estimation/03-RESEARCH.md`
</canonical_refs>

<deferred>
## Deferred Ideas
- **D-07:** Distributed Inference: Revisit if the single-server CPU becomes a bottleneck under high machine counts (GPU acceleration or separate inference worker).
- **D-08:** Model Auto-retraining: Initially, models are manually uploaded; automated retraining will be considered for v2.0.
</deferred>
