from src.services.processing_service import signal_processor
from src.services.anomaly_service import anomaly_detector
from src.services.deep_learning_service import rul_service
from src.core.executor import get_ml_executor
from src.core.connection_manager import connection_manager
import logging
import numpy as np
import asyncio
from datetime import datetime

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
            # Broadcast Anomaly Alert
            await connection_manager.broadcast({
                "type": "ANOMALY",
                "machine_id": machine_id,
                "sensor": sensor_type,
                "severity": "CRITICAL",
                "timestamp": datetime.now().isoformat(),
                "details": f"Anomaly detected in {sensor_type} signal."
            })

        # 5. RUL Estimation (Last 30 Windows)
        seq_key = f"{machine_id}:{sensor_type}:seq"
        if seq_key not in _sequence_buffers:
            _sequence_buffers[seq_key] = []
        
        _sequence_buffers[seq_key].append(features)
        if len(_sequence_buffers[seq_key]) > 30:
            _sequence_buffers[seq_key] = _sequence_buffers[seq_key][-30:]
            
        if len(_sequence_buffers[seq_key]) == 30:
            loop = asyncio.get_event_loop()
            rul = await loop.run_in_executor(
                get_ml_executor(),
                rul_service.estimate_rul,
                _sequence_buffers[seq_key]
            )
            
            # Broadcast RUL Updates / Alerts
            alert_payload = {
                "type": "RUL_UPDATE",
                "machine_id": machine_id,
                "sensor": sensor_type,
                "rul": round(rul, 1),
                "timestamp": datetime.now().isoformat()
            }
            
            if rul < 20.0:
                logger.critical(f"⚠️ [CRITICAL] Machine ID: {machine_id} | Predicted RUL: {rul:.1f} cycles | FAILURE IMMINENT")
                alert_payload.update({"type": "URGENT_MAINTENANCE", "severity": "CRITICAL"})
            elif rul < 50.0:
                alert_payload.update({"severity": "WARNING"})
            else:
                alert_payload.update({"severity": "INFO"})
                
            await connection_manager.broadcast(alert_payload)
            
    except Exception as e:
        logger.error(f"Error in background task processing telemetry: {e}")
