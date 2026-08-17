from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.installation import InstallationCreate, InstallationResponse
from app.services.installation_service import installation_service


router = APIRouter(
    prefix="/installation",
    tags=["Installations"]
)


@router.post(
    "",
    response_model=InstallationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_installation(installation: InstallationCreate, db: Session = Depends(get_db)):
    return installation_service.create_installation(db, installation)
    