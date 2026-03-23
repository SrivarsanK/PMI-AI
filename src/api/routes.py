from fastapi import APIRouter, Depends, Security, HTTPException, status, BackgroundTasks
from typing import List
from src.models.telemetry import TelemetryIn
from src.models.health import MachineHealthSummary
from src.models.maintenance import MaintenancePrio
from src.services.influx_service import influx_db_service
from src.core.security import verify_api_key
from src.core.tasks import process_telemetry_task, _sequence_buffers
from src.services.anomaly_service import anomaly_detector
from src.services.maintenance_service import maintenance_manager
from datetime import datetime

router = APIRouter(prefix="/telemetry", tags=["Health & Maintenance API"])

@router.post("/ingest", status_code=status.HTTP_201_CREATED)
async def ingest_telemetry(
    data: TelemetryIn,
    background_tasks: BackgroundTasks,
    api_key: str = Security(verify_api_key)
):
    try:
        await influx_db_service.write_point(
            machine_id=data.machine_id,
            sensor_type=data.sensor_type,
            value=data.value
        )
        background_tasks.add_task(
            process_telemetry_task,
            machine_id=data.machine_id,
            sensor_type=data.sensor_type,
            value=data.value
        )
        return {
            "status": "success",
            "message": "Telemetry point recorded",
            "machine": data.machine_id
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/maintenance/schedule", response_model=List[MaintenancePrio])
async def get_maintenance_schedule(api_key: str = Security(verify_api_key)):
    """
    Returns a list of machines ranked by failure risk and maintenance urgency.
    """
    try:
        return maintenance_manager.get_maintenance_ranking()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/analytics/mtbf/{machine_id}")
async def get_machine_mtbf(machine_id: str, api_key: str = Security(verify_api_key)):
    """
    Returns the estimated MTBF for a specific machine.
    """
    try:
        mtbf = await maintenance_manager.calculate_mtbf(machine_id)
        return {"machine_id": machine_id, "mtbf_hours": mtbf}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/analytics/reliability")
async def get_reliability_trends(api_key: str = Security(verify_api_key)):
    """
    Returns high-level reliability trends for the facility.
    """
    # Placeholder for aggregate reliability scoring
    return {"facility_score": 0.92, "trend": "Stable"}

@router.get("/machines", response_model=List[MachineHealthSummary])
async def list_machines(api_key: str = Security(verify_api_key)):
    """
    Returns a summary of all active machines in the system.
    """
    # (Existing implementation)
    machines = []
    unique_ids = set()
    for key in anomaly_detector._buffers.keys():
        m_id = key.split(':')[0]
        unique_ids.add(m_id)
        
    for m_id in unique_ids:
        machines.append(MachineHealthSummary(
            machine_id=m_id,
            status="Healthy",
            last_rul=130.0,
            is_anomalous=False,
            last_update=datetime.now()
        ))
    return machines

@router.get("/machines/{machine_id}/history")
async def get_machine_history(
    machine_id: str, 
    api_key: str = Security(verify_api_key)
):
    # (Existing implementation)
    try:
        return {"machine_id": machine_id, "data": "Time-series data retrieved from InfluxDB"}
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
