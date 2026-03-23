from src.services.processing_service import signal_processor
from src.services.anomaly_service import anomaly_detector
import logging
import numpy as np

logger = logging.getLogger(__name__)

async def process_telemetry_task(machine_id: str, sensor_type: str, value: float):
    """
    Background Task: Process a single telemetry ingestion.
    Coordinates signal filtering, feature extraction, and anomaly detection.
    
    1. Update the machine/sensor buffer.
    2. Apply Butterworth filter.
    3. Extract features (mean, std, rms).
    4. Run anomaly detection.
    5. Log critical failures.
    """
    
    try:
        # 1. Update machine buffer with new point
        window = anomaly_detector.add_to_buffer(machine_id, sensor_type, value)
        
        # We need a minimum number of points to filter effectively
        if len(window) < 10:
            return
            
        data_arr = np.array(window)

        # 2. Apply digital noise filter
        filtered_data = signal_processor.apply_butterworth_filter(
            data_arr, fs=100.0, cutoff=10.0
        )
        
        # 3. Extract features from the filtered window
        features = signal_processor.extract_features(filtered_data)
        
        # 4. Predict anomaly
        is_anomaly = anomaly_detector.detect(features)
        
        if is_anomaly:
            logger.warning(
                f"[ANOMALY DETECTED] Machine ID: {machine_id} | Sensor: {sensor_type} | "
                f"Features: [Mean: {features[0]:.2f}, Std: {features[1]:.2f}, RMS: {features[2]:.2f}]"
            )
            # Future: Send alerts to Phase 4 (Alerting System)
            
    except Exception as e:
        logger.error(f"Error in background background task processing telemetry: {e}")
