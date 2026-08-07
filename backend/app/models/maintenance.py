from datetime import date
from decimal import Decimal

from sqlalchemy import Boolean, Date, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel
from app.models.enums import MaintenanceType, PaymentMethod


class MaintenanceRecord(BaseModel):
    __tablename__ = "maintenance_records"

    equipment_id: Mapped[int] = mapped_column(
        ForeignKey("equipments.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    maintenance_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    maintenance_type: Mapped[MaintenanceType] = mapped_column(
        Enum(MaintenanceType, name="maintenance_type_enum"),
        nullable=False,
        index=True,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    payment_method: Mapped[PaymentMethod] = mapped_column(
        Enum(PaymentMethod, name="payment_method_enum"),
        nullable=False,
    )

    water_filled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    voltage_checked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    voltage_reading: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    terminal_cleaned: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    battery_replaced: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    wiring_checked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    fuse_changed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    complaint_resolved: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    next_due_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    equipment: Mapped["Equipment"] = relationship(
        back_populates="maintenance_records",
    )