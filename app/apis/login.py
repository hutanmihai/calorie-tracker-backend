from uuid import UUID

from fastapi import APIRouter, Depends, status
from google.auth.transport import requests
from google.oauth2 import id_token

from app.apis.utils.utils import generate_api_error_response, generate_error_responses
from app.auth.auth_bearer import auth_required
from app.auth.jwt_handler import token_encode
from app.services.errors import UserNotFound
from app.services.user_srv import UserSrv
from app.settings import settings

GOOGLE_CLIENT_ID = settings.google_client_id

router = APIRouter()


@router.post(
    "/login",
    summary="Login with Google",
    status_code=status.HTTP_200_OK,
    response_description="Login successful",
    responses=generate_error_responses(
        status.HTTP_400_BAD_REQUEST, status.HTTP_403_FORBIDDEN
    ),
)
async def login_google(token: str, user_srv: UserSrv = Depends(UserSrv)):
    try:
        # Verify the token
        id_info = id_token.verify_oauth2_token(
            token, requests.Request(), GOOGLE_CLIENT_ID
        )

        try:
            if "iss" not in id_info:
                raise ValueError("Invalid token")

            if id_info["iss"] not in [
                "accounts.google.com",
                "https://accounts.google.com",
            ]:
                raise ValueError("Wrong issuer")
        except ValueError as e:
            return generate_api_error_response(status.HTTP_400_BAD_REQUEST, str(e))

        # Check if user exists
        try:
            user = await user_srv.get_user_by_email(id_info["email"])
        except UserNotFound:
            user = await user_srv.new_user(
                id_info["sub"], id_info["email"], id_info["name"], id_info["picture"]
            )

        # Return JWT token
        return token_encode(user.id)

    except ValueError as e:
        return generate_api_error_response(status.HTTP_400_BAD_REQUEST, str(e))


@router.get("/protected", summary="Protected endpoint test")
async def protected(
    user_id: UUID = Depends(auth_required), user_srv: UserSrv = Depends(UserSrv)
):
    user = await user_srv.get_user(user_id)
    return {"message": f"Hello {user.name} from a protected endpoint!"}