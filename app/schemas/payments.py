from pydantic import BaseModel


class PaymentCreate(BaseModel):
    orderId: int
    amount: float
    type: str = "bank-card"  # или "cash", "e-money" — по документации CRM


class PaymentCreateResponse(BaseModel):
    success: bool
    id: int | None = None
    errorMsg: str | None = None
