from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from influxdb_client import Point, WriteOptions
from src.core.config import settings
import logging

logger = logging.getLogger(__name__)

class InfluxDBService:
    def __init__(self):
        self.url = settings.INFLUXDB_URL
        self.token = settings.INFLUXDB_TOKEN
        self.org = settings.INFLUXDB_ORG
        self.bucket = settings.INFLUXDB_BUCKET
        self.client = None

    async def connect(self):
        if not self.client:
            self.client = InfluxDBClientAsync(
                url=self.url,
                token=self.token,
                org=self.org
            )

    async def close(self):
        if self.client:
            await self.client.close()
            self.client = None

    async def write_point(self, machine_id: str, sensor_type: str, value: float):
        if not self.client:
            await self.connect()

        point = (
            Point("telemetry")
            .tag("machine_id", machine_id)
            .tag("sensor_type", sensor_type)
            .field("value", value)
        )

        try:
            write_api = self.client.write_api()
            await write_api.write(bucket=self.bucket, org=self.org, record=point)
        except Exception as e:
            logger.error(f"Error writing to InfluxDB: {e}")
            raise

influx_db_service = InfluxDBService()
