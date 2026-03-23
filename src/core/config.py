from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "PMI-AI: Predictive Maintenance Intelligence System"
    API_KEY: str = "pmi_ai_default_secret_key_2026"
    DEBUG: bool = True
    
    # InfluxDB Settings (to be used in 01-02)
    INFLUXDB_URL: str = "http://localhost:8086"
    INFLUXDB_TOKEN: Optional[str] = None
    INFLUXDB_ORG: Optional[str] = "pmi-ai"
    INFLUXDB_BUCKET: Optional[str] = "telemetry"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
