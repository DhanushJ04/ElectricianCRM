from datetime import date

from sqlalchemy import Boolean, Date, Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel
from app.models.enums import CustomerStatus


class Customer(BaseModel):
    __tablename__ = "customers"

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True,
        index=True,
    )

    address: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    installation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[CustomerStatus] = mapped_column(
        Enum(
            CustomerStatus,
            name="customer_status_enum",
        ),
        default=CustomerStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    equipments: Mapped[list["Equipment"]] = relationship(
    back_populates="customer",
    cascade="all, delete-orphan",
)