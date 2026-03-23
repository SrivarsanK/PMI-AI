import torch
import torch.nn as nn
from typing import Optional
import os

class RULPredictorLSTM(nn.Module):
    """
    LSTM-based architecture for Remaining Useful Life (RUL) estimation.
    """
    def __init__(self, input_dim: int = 3, hidden_dim: int = 128, num_layers: int = 2):
        super(RULPredictorLSTM, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        
        # LSTM layer: input_dim (features like mean, std, rms)
        self.lstm = nn.LSTM(
            input_dim, 
            hidden_dim, 
            num_layers, 
            batch_first=True, 
            dropout=0.2 if num_layers > 1 else 0
        )
        
        # Fully connected layer for regression
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor):
        # x shape: (batch, sequence_length, input_dim)
        # Initialize hidden and cell states
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))
        
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out

def load_model(path: Optional[str] = None, input_dim: int = 3) -> RULPredictorLSTM:
    """
    Factory method to load the RUL LSTM model.
    """
    model = RULPredictorLSTM(input_dim=input_dim)
    if path and os.path.exists(path):
        try:
            model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
            model.eval()
        except Exception as e:
            print(f"Warning: Could not load weights from {path}: {e}")
    return model
