from csv import DictReader

from sqlalchemy.exc import IntegrityError

from app.database import async_session
from app.models import Product

PRODUCTS_PATH = "../../data/food.csv"


async def get_products_data():
    """
    Get products data from CSV file

    Returns:
        List of dictionaries for <Product>
    """
    with open(PRODUCTS_PATH, "r", encoding="utf-8") as csv_file:
        reader = DictReader(csv_file, delimiter="\t")

        products = []

        for row in reader:
            product = {
                "product_name": row["product_name"],
                "energy_kcal": round(float(row["energy-kcal_100g"]), 2),
                "fat": round(float(row["fat_100g"]), 2),
                "carbohydrates": round(float(row["carbohydrates_100g"]), 2),
                "protein": round(float(row["proteins_100g"]), 2),
                "downvotes": 0,
            }
            if (
                product["fat"] == 0
                and product["carbohydrates"] == 0
                and product["protein"] == 0
            ):
                continue
            if product["energy_kcal"] == 0:
                continue
            product["product_name"] = product["product_name"].strip().lower()
            pn = product["product_name"]
            if pn in ["", "0", 0, "?", ".", "#", "nan", "none", "null", "undefined"]:
                continue
            products.append(product)

    return products


async def fill_db_with_products():
    """
    Save object into database

    # get all products data
    # save each product
    """
    products = await get_products_data()

    async with async_session() as session:
        async with session.begin():

            for product in products:
                prod = Product(**product)
                session.add(prod)

            try:
                await session.commit()
            except IntegrityError:
                await session.rollback()


async def fill_db():
    await fill_db_with_products()


if __name__ == "__main__":
    import asyncio

    asyncio.run(fill_db())
