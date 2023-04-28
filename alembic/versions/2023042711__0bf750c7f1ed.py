"""empty message

Revision ID: 0bf750c7f1ed
Revises: 0524ea6a9689
Create Date: 2023-04-27 20:11:36.769638

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0bf750c7f1ed"
down_revision = "0524ea6a9689"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "diary",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("date", sa.DATE(), nullable=False),
        sa.Column("total_calories", sa.FLOAT(decimal_return_scale=2), nullable=False),
        sa.Column("total_fat", sa.FLOAT(decimal_return_scale=2), nullable=False),
        sa.Column("total_carbs", sa.FLOAT(decimal_return_scale=2), nullable=False),
        sa.Column("total_protein", sa.FLOAT(decimal_return_scale=2), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "date", name="unique_user_date_diary"),
    )
    op.create_table(
        "diary_product",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("diary_id", sa.UUID(), nullable=False),
        sa.Column("product_id", sa.UUID(), nullable=False),
        sa.Column("quantity_grams", sa.FLOAT(decimal_return_scale=2), nullable=False),
        sa.ForeignKeyConstraint(
            ["diary_id"],
            ["diary.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("diary_product")
    op.drop_table("diary")
    # ### end Alembic commands ###