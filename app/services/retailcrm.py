import json
from urllib.parse import urlencode

import httpx

from core import settings
from schemas import CustomerCreate, CustomerFilter
from schemas.orders import OrderCreate
from schemas.payments import PaymentCreate


class RetailCRMClient:
    """Client for interacting with the RetailCRM API."""

    GET_CUSTOMERS = "/customers"
    POST_CREATE_CUSTOMERS = "/customers/create"
    GET_ORDERS = "/orders"
    POST_CREATE_ORDERS = "/orders/create"
    POST_CREATE_ORDERS_PAYMENTS = "/orders/payments/create"

    def __init__(self) -> None:
        self.client: httpx.AsyncClient | None = None

    async def _post(self, path: str, data: dict):
        payload = urlencode(
            {
                k: json.dumps(v) if isinstance(v, (dict, list)) else v
                for k, v in data.items()
            }
        )
        response = await self.client.post(
            url=path,
            data=payload,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        return response.json()

    async def _get(self, path: str, filters: dict | None = None):
        params = {}
        if filters:
            params = {f"filter[{key}]": value for key, value in filters.items()}
        response = await self.client.get(url=path, params=params)
        return response.json()

    # --- CUSTOMERS ---

    async def create_customer(self, customer_in: CustomerCreate):
        payload = {
            "site": customer_in.site,
            "customer": customer_in.customer.model_dump(),
        }
        return await self._post(self.POST_CREATE_CUSTOMERS, payload)

    async def get_customers(self, filters: CustomerFilter | None = None):
        filters_dict = filters.model_dump(exclude_none=True) if filters else {}
        return await self._get(self.GET_CUSTOMERS, filters_dict)

    # --- ORDERS ---

    async def get_orders_by_customer(self, customer_id: int):
        return await self._get(self.GET_ORDERS, {"customerId": customer_id})

    async def create_order(self, data: OrderCreate):
        order_data = {
            "site": data.site,
            "number": data.number,
            "customer": {"id": data.customerId},
            "items": [item.model_dump(exclude_none=True) for item in data.items],
        }
        return await self._post(self.POST_CREATE_ORDERS, {"order": order_data})

    # --- PAYMENTS ---

    async def create_payment(self, data: PaymentCreate):
        payment_data = {
            "order": {"id": data.orderId},
            "amount": data.amount,
            "type": data.type,
        }
        return await self._post(
            self.POST_CREATE_ORDERS_PAYMENTS, {"payment": payment_data}
        )

    # --- CONTEXT MANAGER ---

    async def __aenter__(self):
        self.client = httpx.AsyncClient(
            base_url=settings.retailcrm.api_url,
            headers={"X-Api-Key": settings.retailcrm.api_key},
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()
