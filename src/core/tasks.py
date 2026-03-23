from src.services.processing_service import signal_processor
from src.services.anomaly_service import anomaly_detector
from src.services.deep_learning_service import rul_service
from src.core.executor import get_ml_executor
import logging
import numpy as np
import asyncio

logger = logging.getLogger(__name__)

# Cache for filtered feature sequences to feed the LSTM (Size: 30)
_sequence_buffers = {}

async def process_telemetry_task(machine_id: str, sensor_type: str, value: float):
    """
    Background Task: Process a single telemetry ingestion.
    Coordinates signal filtering, feature extraction, anomaly detection, and RUL estimation.
    """
    
    try:
        # 1. Update machine buffer with new point
        window = anomaly_detector.add_to_buffer(machine_id, sensor_type, value)
        
        # Minimum points to filter effectively
        if len(window) < 10:
            return
            
        data_arr = np.array(window)

        # 2. Apply digital noise filter (Butterworth)
        filtered_data = signal_processor.apply_butterworth_filter(
            data_arr, fs=100.0, cutoff=10.0
        )
        
        # 3. Extract features (mean, std, rms)
        features = signal_processor.extract_features(filtered_data)
        
        # 4. Predict anomaly (unsupervised Isolation Forest)
        is_anomaly = anomaly_detector.detect(features)
        
        if is_anomaly:
            logger.warning(
                f"[ANOMALY DETECTED] Machine ID: {machine_id} | Sensor: {sensor_type} | "
                f"Features: [Mean: {features[0]:.2f}, Std: {features[1]:.2f}, RMS: {features[2]:.2f}]"
            )

        # 5. RUL Estimation (Last 30 Windows)
        # Store sequences of features (mean, std, rms vectors)
        seq_key = f"{machine_id}:{sensor_type}:seq"
        if seq_key not in _sequence_buffers:
            _sequence_buffers[seq_key] = []
        
        _sequence_buffers[seq_key].append(features)
        if len(_sequence_buffers[seq_key]) > 30:
            _sequence_buffers[seq_key] = _sequence_buffers[seq_key][-30:]
            
        # Run deep learning inference in thread pool (CPU bound)
        if len(_sequence_buffers[seq_key]) == 30:
            loop = asyncio.get_event_loop()
            rul = await loop.run_in_executor(
                get_ml_executor(),
                rul_service.estimate_rul,
                _sequence_buffers[seq_key]
            )
            
            # Real-time RUL Update
            if rul < 20.0:
                logger.critical(f"⚠️ [CRITICAL] Machine ID: {machine_id} | Predicted RUL: {rul:.1f} cycles | FAILURE IMMINENT")
            else:
                logger.info(f"Machine ID: {machine_id} | Current RUL Estimate: {rul:.1f} cycles")
            
    except Exception as e:
        logger.error(f"Error in background task processing telemetry: {e}")
