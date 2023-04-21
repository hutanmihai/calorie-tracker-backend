from typing import List

from sqlalchemy import select

from app.database import async_session
from app.models import Product


async def get_all_products() -> List[Product]:
    async with async_session() as session:
        return (await session.scalars(select(Product))).all()
