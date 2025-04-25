from typing import Annotated

from fastapi import APIRouter, Query
from fastapi import status

from schemas import (
    CustomerCreate,
    CustomerFilter,
    CustomerCreateResponse,
    CustomerListResponse,
)
from services import RetailCRMClient

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post(
    "/create",
    response_model=CustomerCreateResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_customer(customer_in: CustomerCreate):
    async with RetailCRMClient() as client:
        return await client.create_customer(customer_in)


@router.get(
    "/",
    response_model=CustomerListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_customers(filters: Annotated[CustomerFilter, Query()]):
    async with RetailCRMClient() as client:
        return await client.get_customers(filters)
