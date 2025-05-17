# shipping.py
import asyncio
import random
from logging import getLogger

from asyncio_signal_bus import SignalBus

from asyncio_signal_bus_example.order_example.model import Order

LOGGER = getLogger(__name__)

SHIPPING_BUS = SignalBus()


@SHIPPING_BUS.subscriber(topic_name="order")
async def notify_shipping_system(order: Order):
    await asyncio.sleep(random.randint(0, 100) / 50)
    LOGGER.info(f"notifying shipping system of order {order.order_id}")
