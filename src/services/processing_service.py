import numpy as np
from scipy import signal
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class SignalProcessor:
    """
    Handles digital signal processing for sensor telemetry.
    """

    @staticmethod
    def apply_butterworth_filter(
        data: np.ndarray, 
        fs: float = 100.0, 
        cutoff: float = 10.0, 
        order: int = 2
    ) -> np.ndarray:
        """
        Applies a low-pass Butterworth filter using Second-Order Sections (SOS).
        
        :param data: Input raw signal.
        :param fs: Sampling frequency in Hz.
        :param cutoff: Cutoff frequency in Hz.
        :param order: Filter order.
        :return: Filtered signal.
        """
        if len(data) < order * 3: # Rule of thumb for stable filtering
            return data
            
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        
        # Design SOS filter for numerical stability
        sos = signal.butter(order, normal_cutoff, btype='low', output='sos')
        
        # Apply filter forward and backward (zero-phase)
        filtered_data = signal.sosfiltfilt(sos, data)
        return filtered_data

    @staticmethod
    def extract_features(data: np.ndarray) -> np.ndarray:
        """
        Extracts rolling statistical features: [mean, std, rms].
        
        :param data: Filtered signal window.
        :return: Feature vector as numpy array.
        """
        if len(data) == 0:
            return np.array([0.0, 0.0, 0.0])
            
        mean = np.mean(data)
        std = np.std(data)
        rms = np.sqrt(np.mean(np.square(data)))
        
        return np.array([mean, std, rms])

signal_processor = SignalProcessor()
