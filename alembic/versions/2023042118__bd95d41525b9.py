"""empty message

Revision ID: bd95d41525b9
Revises: 1458f256cf80
Create Date: 2023-04-21 16:18:50.148355

"""
import sqlalchemy as sa
import sqlalchemy_utils

from alembic import op
from app.apis.utils.enums import HeightMetric, WeightMetric

# revision identifiers, used by Alembic.
revision = "bd95d41525b9"
down_revision = "1458f256cf80"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column(
            "pref_height_metric",
            sqlalchemy_utils.types.choice.ChoiceType(HeightMetric),
            nullable=True,
        ),
    )
    op.add_column(
        "user", sa.Column("height", sa.FLOAT(decimal_return_scale=2), nullable=True)
    )
    op.add_column(
        "user",
        sa.Column(
            "pref_weight_metric",
            sqlalchemy_utils.types.choice.ChoiceType(WeightMetric),
            nullable=True,
        ),
    )
    op.add_column(
        "user", sa.Column("weight", sa.FLOAT(decimal_return_scale=2), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "weight")
    op.drop_column("user", "pref_weight_metric")
    op.drop_column("user", "height")
    op.drop_column("user", "pref_height_metric")
    # ### end Alembic commands ###
