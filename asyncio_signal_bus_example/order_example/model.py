# model.py
from datetime import datetime

from pydantic import BaseModel


class Order(BaseModel):
    order_id: str
    customer_id: str
    customer_name: str
    items: list
    updated_at: datetime
