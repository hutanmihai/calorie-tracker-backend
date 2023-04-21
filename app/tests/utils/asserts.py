from typing import List

from app.models import BaseModel, Product, User


def assert_api_validation_error(content: dict, expected_breaking_fields: List[str]):
    for i, _ in enumerate(expected_breaking_fields):
        assert content["detail"][i]["loc"][0] == "body"
        assert content["detail"][i]["loc"][1] == expected_breaking_fields[i]


def assert_api_path_param_validation_error(
    content: dict, expected_breaking_fields: List[str]
):
    for i, _ in enumerate(expected_breaking_fields):
        assert content["detail"][i]["loc"][0] == "path"
        assert content["detail"][i]["loc"][1] == expected_breaking_fields[i]


def assert_api_error(
    content: dict, expected_status_code: int, expected_description: str
):
    assert content["status_code"] == expected_status_code
    assert content["description"] == expected_description


def assert_http_exception_error(content: dict, expected_detail: str):
    assert content["detail"] == expected_detail


def assert_base_product_response(actual_product: Product, expected_product: Product):
    assert actual_product.id is not None
    assert actual_product.name == expected_product.name
    assert actual_product.calories == expected_product.calories
    assert actual_product.fat == expected_product.fat
    assert actual_product.carbs == expected_product.carbs
    assert actual_product.protein == expected_product.protein
    assert actual_product.upvotes == expected_product.upvotes
    assert actual_product.downvotes == expected_product.downvotes


def assert_list_all_products_response(
    actual_products: List[Product], expected_products: List[Product]
):
    assert actual_products is not None
    assert len(actual_products) == len(expected_products)

    for actual_product, expected_product in zip(actual_products, expected_products):
        assert actual_product.id is not None
        assert actual_product.name == expected_product.name
        assert actual_product.calories == expected_product.calories
        assert actual_product.fat == expected_product.fat
        assert actual_product.carbs == expected_product.carbs
        assert actual_product.protein == expected_product.protein
        assert actual_product.upvotes == expected_product.upvotes
        assert actual_product.downvotes == expected_product.downvotes


def assert_id_did_not_change(actual: BaseModel, expected: BaseModel):
    assert actual.id == str(expected.id)
