from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.equipment import Equipment



class EquipmentRepository:
    """
    Repository responsible for Equipment database operations.

    This repository does not commit transactions.
    The service layer controls the transaction.
    """

    def create(self, db: Session, equipment: Equipment) -> Equipment:

        db.add(equipment)

        db.flush()

        db.refresh(equipment)

        return equipment


    def get_by_id(self, db: Session, equipment_id: int) -> Equipment | None:

        return db.get(Equipment, equipment_id)


    def get_by_customer(self, db: Session, customer_id: int) -> list[Equipment]:

        stmt = (select(Equipment).where(Equipment.customer_id == customer_id).order_by(Equipment.installation_date))

        return db.scalars(stmt).all()



equipment_repository = EquipmentRepository()