from datetime import date

from sqlalchemy import Date, Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel
from app.models.enums import EquipmentStatus, EquipmentType


class Equipment(BaseModel):
    __tablename__ = "equipments"

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    equipment_type: Mapped[EquipmentType] = mapped_column(
        Enum(EquipmentType, name="equipment_type_enum"),
        nullable=False,
    )

    brand: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    model: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    capacity: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    serial_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        unique=True,
        index=True,
    )

    installation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    warranty_end: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[EquipmentStatus] = mapped_column(
        Enum(EquipmentStatus, name="equipment_status_enum"),
        default=EquipmentStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="equipments",
    )

    maintenance_records: Mapped[list["MaintenanceRecord"]] = relationship(
        back_populates="equipment",
        cascade="all, delete-orphan",
    )