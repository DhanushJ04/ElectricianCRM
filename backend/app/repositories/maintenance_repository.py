from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.maintenance import MaintenanceRecord


class MaintenanceRepository:
    """
    Repository for Maintenance database operations.
    """

    def create(self, db: Session, maintenance: MaintenanceRecord) -> MaintenanceRecord:

        db.add(maintenance)

        db.flush()

        db.refresh(maintenance)

        return maintenance


    def get_by_equipment(self, db: Session, equipment_id: int) -> list[MaintenanceRecord]:

        stmt = (
            select(MaintenanceRecord).where(MaintenanceRecord.equipment_id == equipment_id).order_by(MaintenanceRecord.maintenance_date.desc()))

        return db.scalars(stmt).all()


maintenance_repository = MaintenanceRepository()