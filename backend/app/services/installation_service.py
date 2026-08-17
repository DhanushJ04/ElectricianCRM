from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.models.equipment import Equipment
from app.models.maintenance import MaintenanceRecord
from app.models.enums import MaintenanceType, PaymentMethod

from app.repositories.customer_repository import customer_repository
from app.repositories.equipment_repository import equipment_repository
from app.repositories.maintenance_repository import maintenance_repository

from app.schemas.installation import InstallationCreate

from app.utils.date_utils import calculate_next_maintenance_date


class InstalltionService:
    """
    Handles the complete new-installtion workflow
    """

    def create_installation(self, db: Session, installation: InstallationCreate):
        """
        Create a customer, their equipment, and intial installtion maintenance records.
        """

        # --------------------------------------------------
        # 1. Check whether customer already exists
        # --------------------------------------------------

        existing_customer = customer_repository.get_by_phone(db, installation.customer.phone)

        if existing_customer:
            raise HTTPException(
                status_code=409,
                detail="Customer with this phone number already exists.",
            )

        try:
            # --------------------------------------------------
            # 2. Create Customer
            # --------------------------------------------------

            customer = Customer(
                full_name=installation.customer.full_name,
                phone=installation.customer.phone,
                address=installation.customer.address,
                installation_date=installation.customer.installation_date,
                notes=installation.customer.notes,
            )

            customer = customer_repository.create(db, customer)

            # --------------------------------------------------
            # 3. Create Equipment
            # --------------------------------------------------

            created_equipments = []

            for equipment_data in installation.equipments:

                equipment = Equipment(
                    customer_id=customer.id,
                    equipment_type=equipment_data.equipment_type,
                    brand=equipment_data.brand,
                    model=equipment_data.model,
                    capacity=equipment_data.model,
                    serial_number=equipment_data.serial_number,
                    installation_date=installation.customer.installation_date,
                    warranty_end=equipment_data.warranty_end,
                    notes=equipment_data.notes,
                )

                equipment = equipment_repository.create(db, equipment)

                created_equipments.append(equipment)

                # --------------------------------------------------
                # 4. Create Installation Maintenance Record
                # --------------------------------------------------

                next_due_date = calculate_next_maintenance_date(installation.customer.installation_date)

                maintenance = MaintenanceRecord(
                    equipment_id=equipment.id,
                    maintenance_date=installation.customer.installation_date,
                    maintenance_type=MaintenanceType.INSTALLATION,
                    amount=0,
                    payment_method=PaymentMethod.PENDING,
                    next_due_date=next_due_date,
                    notes="Initial installation"
                )

                maintenance_repository.create(db, maintenance)

             # --------------------------------------------------
            # 5. Commit the COMPLETE transaction
            # --------------------------------------------------

            db.commit()

            # Refresh customer after commit
            db.refresh(customer)

            return {
                "customer": customer,
                "equipments": created_equipments
            }

        except Exception:
            # ----------------------------------------------
            # Something failed.
            # Undo everything created in this transaction.
            # ----------------------------------------------

            db.rollback()

            raise

        

installation_service = InstalltionService()