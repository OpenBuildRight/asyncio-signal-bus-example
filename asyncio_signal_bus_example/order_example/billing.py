# billing.py
import asyncio
import random
from logging import getLogger

from asyncio_signal_bus import SignalBus

from asyncio_signal_bus_example.order_example.model import Order

LOGGER = getLogger(__name__)

BILLING_BUS = SignalBus()


@BILLING_BUS.subscriber(topic_name="order")
async def notify_billing_system(order: Order):
    await asyncio.sleep(random.randint(0, 100) / 50)
    LOGGER.info(f"notifying billing system of order {order.order_id}")
