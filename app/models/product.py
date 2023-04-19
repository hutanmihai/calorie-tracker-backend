import uuid

from sqlalchemy import DECIMAL, INT, VARCHAR, Column
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name = Column(VARCHAR(255), nullable=False)
    energy_kcal = Column(
        DECIMAL(precision=None, scale=None, asdecimal=True), nullable=False
    )
    fat = Column(DECIMAL(precision=None, scale=None, asdecimal=True), nullable=False)
    carbohydrates = Column(
        DECIMAL(precision=None, scale=None, asdecimal=True), nullable=False
    )
    protein = Column(
        DECIMAL(precision=None, scale=None, asdecimal=True), nullable=False
    )
    downvotes = Column(INT(), nullable=False)
