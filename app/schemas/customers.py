from pydantic import BaseModel, Field, EmailStr, constr
from enum import Enum
from datetime import datetime


class ContragentType(str, Enum):
    individual = "individual"
    legal_entity = "legal-entity"
    entrepreneur = "entrepreneur"


class Contragent(BaseModel):
    contragentType: ContragentType = ContragentType.individual


class Phone(BaseModel):
    number: constr(pattern=r"^\+?[1-9]\d{7,14}$")


class CustomerItem(BaseModel):
    firstName: str
    lastName: str | None = None
    email: EmailStr | None = None
    phones: list[Phone] = Field(default_factory=list)
    contragent: Contragent = Contragent()


class CustomerCreate(BaseModel):
    customer: CustomerItem
    site: str | None = "simple-site"


class CustomerResponse(BaseModel):
    id: int
    firstName: str
    lastName: str | None = None
    email: EmailStr | None = None
    site: str | None = None
    phones: list[Phone] = Field(default_factory=list)
    contragent: Contragent
    createdAt: datetime


class CustomerCreateResponse(BaseModel):
    success: bool
    id: int
    errorMsg: str | None = None


class CustomerListResponse(BaseModel):
    success: bool
    customers: list[CustomerResponse]
    pagination: dict


class CustomerFilter(BaseModel):
    name: str | None = Field(None, description="Filter by customer name")
    email: EmailStr | None = Field(None, description="Filter by customer email")
    dateFrom: datetime | None = Field(
        None,
        description="Filter by registration date (from)",
        pattern_example="2014-03-21 05:14:07",
    )
    dateTo: datetime | None = Field(
        None,
        description="Filter by registration date (to)",
        pattern_example="2014-03-21 05:14:07",
    )
