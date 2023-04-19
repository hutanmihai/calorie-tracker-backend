import uuid

from sqlalchemy import VARCHAR, Column
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    g_id = Column(VARCHAR(255), nullable=False, unique=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    name = Column(VARCHAR(255), nullable=False)
    picture = Column(VARCHAR(255), nullable=True)
