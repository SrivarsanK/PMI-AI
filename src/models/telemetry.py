from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class TelemetryIn(BaseModel):
    machine_id: str = Field(..., description="Unique machine identifier.")
    sensor_type: str = Field(..., description="Type of sensor: temperature, vibration, or pressure.")
    value: float = Field(..., description="Numerical sensor value.")
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)

    @field_validator("sensor_type")
    @classmethod
    def validate_sensor_type(cls, v: str) -> str:
        allowed = {"temperature", "vibration", "pressure"}
        if v.lower() not in allowed:
            raise ValueError(f"sensor_type must be one of: {allowed}")
        return v.lower()
