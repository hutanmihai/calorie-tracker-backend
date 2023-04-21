def get_create_user_payload(
    g_id: str | None, email: str | None, name: str | None, picture: str | None
):
    payload = {}
    if g_id is not None:
        payload["g_id"] = g_id
    if email is not None:
        payload["email"] = email
    if name is not None:
        payload["name"] = name
    if picture is not None:
        payload["picture"] = picture
    return payload


def get_create_product_payload(
    name: str | None,
    calories: float | None,
    fat: float | None,
    protein: float | None,
    carbs: float | None,
):
    payload = {}
    if name is not None:
        payload["name"] = name
    if calories is not None:
        payload["calories"] = calories
    if fat is not None:
        payload["fat"] = fat
    if protein is not None:
        payload["protein"] = protein
    if carbs is not None:
        payload["carbs"] = carbs
    return payload


def get_update_product_payload(
    name: str | None,
    calories: float | None,
    fat: float | None,
    protein: float | None,
    carbs: float | None,
    upvotes: int | None,
    downvotes: int | None,
):
    payload = {}
    if name is not None:
        payload["name"] = name
    if calories is not None:
        payload["calories"] = calories
    if fat is not None:
        payload["fat"] = fat
    if protein is not None:
        payload["protein"] = protein
    if carbs is not None:
        payload["carbs"] = carbs
    if upvotes is not None:
        payload["upvotes"] = upvotes
    if downvotes is not None:
        payload["downvotes"] = downvotes
    return payload
