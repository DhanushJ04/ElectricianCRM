from datetime import date

from pydantic import Field

from app.models.enums import EquipmentType, CustomerStatus
from app.schemas.base import BaseSchema, TimestampSchema


class CustomerInformation(BaseSchema): 
    full_name: str = Field(
            min_length=2,
            max_length=100
        )
    
    phone: str = Field(
        min_length=10,
        max_length=20
    )
    
    address: str
    
    installation_date: date
    
    notes: str | None = None 


        
class EquipmentCreate(BaseSchema):
    equipment_type: EquipmentType

    brand: str = Field(
        min_length=2,
        max_length=100,
    )

    model: str | None = None

    capacity: str | None = None

    serial_number: str | None = None

    warranty_end: date | None = None

    notes: str | None = None 



class InstallationCreate(BaseSchema):
    customer: CustomerInformation

    equipments: list[EquipmentCreate] = Field(
        min_length=1
    )



class EquipmentResponse(BaseSchema):
    id: int

    equipment_type: EquipmentType

    brand: str

    model: str | None 

    capacity: str | None

    serial_number: str | None

    installation_date: date

    warranty_end: date | None

    notes: str | None



class CustomerResponse(TimestampSchema):
    id: int

    full_name: str

    phone: str

    address: str

    installation_date: date

    status: CustomerStatus

    is_active: bool

    notes: str | None



class InstallationResponse(BaseSchema):
    customer: CustomerResponse

    equipments: list[EquipmentResponse]