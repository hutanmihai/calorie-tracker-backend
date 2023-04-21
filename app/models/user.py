import uuid

from sqlalchemy import FLOAT, VARCHAR, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import ChoiceType

from app.apis.utils.enums import HeightMetric, WeightMetric
from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    g_id = Column(VARCHAR(255), nullable=False, unique=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    name = Column(VARCHAR(255), nullable=False)
    picture = Column(VARCHAR(255), nullable=True)
    pref_height_metric = Column(ChoiceType(HeightMetric), unique=False, nullable=True)
    height = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=True)
    pref_weight_metric = Column(ChoiceType(WeightMetric), unique=False, nullable=True)
    weight = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=True)
