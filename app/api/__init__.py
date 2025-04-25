from fastapi import APIRouter

from .customers import router as customers_router
from .orders import router as orders_router
from .payments import router as payments_router

router = APIRouter()
router.include_router(customers_router)
router.include_router(orders_router)
router.include_router(payments_router)
