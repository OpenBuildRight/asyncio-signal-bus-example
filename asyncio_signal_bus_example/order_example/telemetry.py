# telemetry.py
import asyncio
import random
from logging import getLogger

from asyncio_signal_bus import SignalBus
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from aiocache import cached

from asyncio_signal_bus_example.order_example.model import Order


LOGGER = getLogger(__name__)

TELEMETRY_BUS = SignalBus()

class TelemetrySettings(BaseSettings, env_prefix="TELEMETRY_"):
    host: str
    password: SecretStr

class TelemetryService(SignalBus):

    def __init__(self, settings: TelemetrySettings):
        self.settings = settings

    async def put_order(self, order: Order):
        await asyncio.sleep(random.randint(0, 100) / 50)
        LOGGER.info(
            f"notifying marketing telemetry system of order {order.order_id} "
            f"using URL {self.settings.host}"
        )

@cached()
async def telemetry_service_factory():
    settings = TelemetrySettings()
    return TelemetryService(settings)


@TELEMETRY_BUS.subscriber(topic_name="order")
@TELEMETRY_BUS.inject("service", telemetry_service_factory)
async def update_marketing_telemetry_system(order: Order, service: TelemetryService):
    await service.put_order(order)