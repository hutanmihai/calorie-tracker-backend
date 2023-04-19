from datetime import datetime

from fastapi import Request, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer

from app.auth.jwt_handler import token_decode


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = token_decode(jwtoken)
        except:
            payload = None
        if payload:
            exp = payload.get("exp")
            is_expired = datetime.utcnow() > datetime.utcfromtimestamp(exp)

            if not is_expired:
                is_token_valid = True
            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token has expired.")

        return is_token_valid


# Function that gets the user_id from the token after it has been decoded
async def auth_required(token: str = Depends(JWTBearer())):
    user_id = token_decode(token).get("sub")

    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing user_id in token")

    return user_id
