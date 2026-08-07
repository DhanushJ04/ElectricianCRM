from datetime import date

from pydantic import Field

from app.models.enums import CustomerStatus
from app.schemas.base import BaseSchema, TimestampSchema


class CustomerCreate(BaseSchema):
    full_name: str = Field(
        min_length=2,
        max_length=100,
    )

    phone: str = Field(
        min_length=10,
        max_length=20,
    )

    address: str

    installation_date: date

    notes: str | None = None



class CustomerUpdate(BaseSchema):
    full_name: str | None = None
    phone: str | None = None
    address: str | None = None
    notes: str | None = None 
    status: CustomerStatus | None = None
    is_active: bool | None = None


class CustomerResponse(TimestampSchema):
    id: int

    full_name: str

    phone: str

    address: str

    installation_date: date

    status: CustomerStatus

    is_active: bool

    notes: str | None