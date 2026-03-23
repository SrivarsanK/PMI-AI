from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class MachineHealthSummary(BaseModel):
    """
    Metadata for a machine's current health status.
    """
    machine_id: str
    status: str # "Healthy", "Warning", "Critical"
    last_rul: float
    is_anomalous: bool
    last_update: datetime

class MachineDetailedHealth(BaseModel):
    """
    Detailed time-series data for a specific machine.
    """
    machine_id: str
    telemetry_history: List[dict] # [{time, value, filtered, is_anomaly, rul}]
