from fastapi import APIRouter
from fastapi import status

from schemas.orders import OrderCreate, OrderCreateResponse, OrderListResponse
from services import RetailCRMClient

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post(
    "/orders/create",
    response_model=OrderCreateResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_order(data: OrderCreate):
    async with RetailCRMClient() as client:
        return await client.create_order(data)


@router.get(
    "/{customer_id}",
    response_model=OrderListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_orders_by_customer(customer_id: int):
    async with RetailCRMClient() as client:
        return await client.get_orders_by_customer(customer_id)
