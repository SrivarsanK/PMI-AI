from fastapi import APIRouter, Depends, Security, HTTPException, status, BackgroundTasks
from src.models.telemetry import TelemetryIn
from src.services.influx_service import influx_db_service
from src.core.security import verify_api_key
from src.core.tasks import process_telemetry_task

router = APIRouter(prefix="/telemetry", tags=["Ingestion API"])

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
        # Trigger background processing (DSP and Anomaly Detection)
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
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
