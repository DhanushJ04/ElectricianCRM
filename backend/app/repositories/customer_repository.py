from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerUpdate


class CustomerRepository:
    """
    Repository responsible for Customer database operations.

    This repository does not commit transactions.
    The service layer controls the transaction. 
    """

    def create(self, db: Session, customer: Customer) -> Customer:
        
        db.add(customer)

        db.flush()

        db.refresh(customer)

        return customer


    def get_by_id(self, db: Session, customer_id: int) -> Customer | None:

        return db.get(Customer, customer_id)


    def get_by_phone(self, db: Session, phone: str) -> Customer | None:
        
        stmt = (select(Customer).where(Customer.phone == phone))

        return db.scalar(stmt)


    def get_all(self, db: Session) -> list[Customer]:
        
        stmt = (select(Customer).order_by(Customer.full_name))

        return db.scalars(stmt).all()


    def update(self, db: Session, customer: Customer, updates: CustomerUpdate) -> Customer:
        
        update_data = updates.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(customer, field, value)

        db.flush()

        db.refresh(customer)

        return customer


    def delete(self, db: Session, customer: Customer) -> None:

        db.delete(customer)

        db.flush()


customer_repository = CustomerRepository()