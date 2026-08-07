from enum import Enum


class EquipmentType(str, Enum):
    BATTERY = "Battery"
    INVERTER = "Inverter"
    SOLAR = "Solar"
    OTHER = "Other"



class MaintenanceType(str, Enum):
    INSTALLATION = "Installation"
    ROUTINE = "Routine"
    EMERGENCY = "Emergency"



class PaymentMethod(str, Enum):
    CASH = "Cash"
    UPI = "UPI"
    BANK_TRANSFER = "Bank Transfer"
    PENDING = "Pending"



class CustomerStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    WARRANTY_EXPIRED = "Warranty Expired"
    NEEDS_REPLACEMENT = "Needs Replacement"



class EquipmentStatus(str, Enum):
    ACTIVE = "Active"
    REPLACED = "Replaced"
    DAMAGED = "Damaged"
    REMOVED = "Removed"
