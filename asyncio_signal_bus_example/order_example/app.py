from contextlib import asynccontextmanager

from asyncio_signal_bus import SignalBus
from fastapi import FastAPI
from pydantic import BaseModel

from asyncio_signal_bus_example.order_example.model import Order
from asyncio_signal_bus_example.order_example.billing import BILLING_BUS
from asyncio_signal_bus_example.order_example.order import ORDER_BUS, create_order
from asyncio_signal_bus_example.order_example.shipping import SHIPPING_BUS
from asyncio_signal_bus_example.order_example.telemetry import TELEMETRY_BUS

from logging import getLogger
LOGGER = getLogger(__name__)

BUS = SignalBus()
BUS.connect(ORDER_BUS, BILLING_BUS, SHIPPING_BUS, TELEMETRY_BUS)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    This will keep the bus in active context the whole time the application
    is running.
    """
    yield await BUS.start()
    await BUS.stop()


APP = FastAPI(lifespan=lifespan)


class CreateOrderDto(BaseModel):
    customer_id: str
    customer_name: str
    items: list


@APP.post("/order", response_model=Order)
async def post_order(dto: CreateOrderDto):
    order = await create_order(dto.customer_id, dto.customer_name, dto.items)
    LOGGER.info(f"HTTP request complete")
    return order
