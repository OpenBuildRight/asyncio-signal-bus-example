# order.py
import asyncio
import random
import uuid
from datetime import datetime
from logging import getLogger

from asyncio_signal_bus import SignalBus

from asyncio_signal_bus_example.order_example.model import Order

LOGGER = getLogger(__name__)

ORDER_BUS = SignalBus()


@ORDER_BUS.publisher(topic_name="order")
async def create_order(customer_id: str, customer_name: str, items: list) -> Order:
    # Do business logic here.
    await asyncio.sleep(random.randint(0, 100) / 500)
    order = Order(
        order_id=uuid.uuid4().hex,
        customer_id=customer_id,
        customer_name=customer_name,
        items=items,
        updated_at=datetime.now(),
    )
    LOGGER.info(f"Order created {order.order_id}")
    return order
