from fastapi import APIRouter, status

from schemas import PaymentCreateResponse, PaymentCreate
from services import RetailCRMClient

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post(
    "/payments/create",
    response_model=PaymentCreateResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_payment(data: PaymentCreate):
    async with RetailCRMClient() as client:
        return await client.create_payment(data)
