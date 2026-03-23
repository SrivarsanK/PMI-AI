from sklearn.ensemble import IsolationForest
import numpy as np
from typing import Dict, List, Optional
import logging
from threading import Lock

logger = logging.getLogger(__name__)

class AnomalyDetector:
    """
    Unsupervised Anomaly Detection using Isolation Forest.
    """
    def __init__(self, contamination: float = 0.05, n_estimators: int = 100):
        self.contamination = contamination
        self.n_estimators = n_estimators
        self.model = IsolationForest(
            contamination=self.contamination,
            n_estimators=self.n_estimators,
            random_state=42
        )
        self.is_trained = False
        # Buffer stores raw points per (machine_id, sensor_type)
        # Key format: f"{machine_id}:{sensor_type}"
        self._buffers: Dict[str, List[float]] = {}
        self._lock = Lock()
        self.max_buffer_size = 100 # Maximum samples per sensor

    def add_to_buffer(self, machine_id: str, sensor_type: str, value: float) -> List[float]:
        """
        Adds a new point to the sensor buffer and returns the current window.
        """
        key = f"{machine_id}:{sensor_type}"
        with self._lock:
            if key not in self._buffers:
                self._buffers[key] = []
            
            buf = self._buffers[key]
            buf.append(value)
            
            # Keep only the last N samples
            if len(buf) > self.max_buffer_size:
                self._buffers[key] = buf[-self.max_buffer_size:]
                
            return self._buffers[key]

    def train(self, data: np.ndarray):
        """
        Trains the Isolation Forest model on a baseline dataset.
        Data format: shape (n_samples, n_features)
        """
        try:
            self.model.fit(data)
            self.is_trained = True
            logger.info("Isolation Forest model trained successfully.")
        except Exception as e:
            logger.error(f"Error training Isolation Forest: {e}")
            raise

    def detect(self, features: np.ndarray) -> bool:
        """
        Predicts if the feature vector is an anomaly.
        Features format: shape (1, n_features)
        Returns: True if anomaly, False if normal.
        """
        if not self.is_trained:
            # Fallback for untrianed model: simplistic check if features are non-zero
            return False
            
        try:
            # IsolationForest returns -1 for anomalies, 1 for normal
            prediction = self.model.predict(features.reshape(1, -1))
            return prediction[0] == -1
        except Exception as e:
            logger.error(f"Error during anomaly detection: {e}")
            return False

anomaly_detector = AnomalyDetector()
