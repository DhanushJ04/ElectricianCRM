from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.mixins import TimestampMixin



class BaseModel(Base, TimestampMixin):
    """Base model inherited by every database table."""

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )