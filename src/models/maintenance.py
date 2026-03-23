from pydantic import BaseModel
from typing import Optional

class MaintenancePrio(BaseModel):
    """
    Model for a prioritized maintenance row.
    """
    machine_id: str
    rul_estimate: float
    urgency_level: str # "EMERGENCY", "URGENT", "RECOMMENDED", "NONE"
    anomaly_count_24h: int
    score: float # Aggregate score for sorting
