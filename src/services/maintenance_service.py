from typing import List, Dict
from src.models.maintenance import MaintenancePrio
from src.services.anomaly_service import anomaly_detector
from src.services.influx_service import influx_db_service
from src.core.tasks import _sequence_buffers
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class MaintenanceManager:
    """
    Logic for ranking and prioritizing machine maintenance.
    """
    def __init__(self):
        # Urgency thresholds (RUL in cycles)
        self.EMERGENCY_THRESH = 10.0
        self.URGENT_THRESH = 20.0
        self.RECOMMENDED_THRESH = 50.0

    def calculate_urgency(self, rul: float) -> str:
        if rul < self.EMERGENCY_THRESH:
            return "EMERGENCY"
        if rul < self.URGENT_THRESH:
            return "URGENT"
        if rul < self.RECOMMENDED_THRESH:
            return "RECOMMENDED"
        return "NONE"

    async def calculate_mtbf(self, machine_id: str) -> float:
        """
        Calculates Mean Time Between Failures for a specific machine.
        MTBF = Total Up Time / Number of Failures
        """
        try:
            # Query number of critical alerts (failure proxies) in the last 30 days
            # Note: For now, we return a deterministic value based on anomaly history
            # In Wave 3, we'd perform a complex Flux query
            
            # Identify active windows
            history = anomaly_detector.get_history(machine_id, "Vibration") # Example sensor
            if not history:
                 return 0.0
                 
            # MTBF = 1000 hours / (anomalies + 1) as a proxy
            anomalies = sum(1 for p in history if p.get("is_anomaly"))
            return 1000.0 / (anomalies + 1)
        except Exception as e:
            logger.error(f"MTBF calc error: {e}")
            return 0.0

    def get_maintenance_ranking(self) -> List[MaintenancePrio]:
        # (Existing ranking logic)
        active_machines = {}
        for key in anomaly_detector._buffers.keys():
            m_id = key.split(':')[0]
            if m_id not in active_machines:
                active_machines[m_id] = {"machine_id": m_id, "rul": 130.0, "anomalies": 0}
        
        ranking = []
        for m_id, stats in active_machines.items():
            urgency = self.calculate_urgency(stats["rul"])
            score = (130.0 - stats["rul"]) + (stats["anomalies"] * 10.0)
            ranking.append(MaintenancePrio(
                machine_id=m_id,
                rul_estimate=stats["rul"],
                urgency_level=urgency,
                anomaly_count_24h=stats["anomalies"],
                score=score
            ))
        ranking.sort(key=lambda x: x.score, reverse=True)
        return ranking

# Singleton instance
maintenance_manager = MaintenanceManager()
