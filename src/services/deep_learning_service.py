import torch
import numpy as np
from typing import List, Optional
from src.models.lstm import load_model, RULPredictorLSTM
import logging

logger = logging.getLogger(__name__)

class RULService:
    """
    Service for real-time Remaining Useful Life (RUL) estimation using Deep Learning.
    """
    def __init__(self, model_path: Optional[str] = None):
        # Initialize model (pre-load weights if available)
        self.model = load_model(model_path)
        self.model.eval()
        # Max RUL threshold based on piecewise linear research (NASA C-MAPSS standard)
        self.max_rul = 130.0

    def prepare_input(self, window: List[np.ndarray]) -> torch.Tensor:
        """
        Normalizes and prepares the sliding window for LSTM inference.
        Expected input: List of feature vectors (mean, std, rms).
        """
        # Convert list of vectors to a single sequence array (SeqLen, Features)
        sequence = np.stack(window)
        
        # Add batch dimension: (1, SeqLen, Features)
        tensor = torch.FloatTensor(sequence).unsqueeze(0)
        return tensor

    def estimate_rul(self, window: List[np.ndarray]) -> float:
        """
        Performs inference to estimate RUL.
        """
        try:
            input_tensor = self.prepare_input(window)
            
            with torch.no_grad():
                prediction = self.model(input_tensor)
                rul_value = prediction.item()
                
            # Clip RUL to safe bounds
            return max(0.0, min(self.max_rul, float(rul_value)))
            
        except Exception as e:
            logger.error(f"Error during RUL estimation: {e}")
            return self.max_rul # Fallback to max healthy RUL

# Singleton instance
rul_service = RULService()
