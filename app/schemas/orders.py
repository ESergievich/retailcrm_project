from datetime import datetime

from pydantic import BaseModel


class OrderItem(BaseModel):
    productName: str
    quantity: float
    initialPrice: float


class OrderCreate(BaseModel):
    customerId: int
    number: str
    site: str = "simple-site"
    items: list[OrderItem]


class OrderResponse(BaseModel):
    id: int
    number: str
    site: str | None = None
    createdAt: datetime | None = None
    status: str | None = None


class OrderCreateResponse(BaseModel):
    success: bool
    order: OrderResponse | None
    errorMsg: str | None = None


class OrderListResponse(BaseModel):
    success: bool
    orders: list[OrderResponse]
    pagination: dict | None
