from datetime import datetime, timedelta
from uuid import UUID

from jwt import decode, encode

from app.settings import settings

SECRET = settings.secret_key
ALGORITHM = settings.algorithm


def token_encode(user_id: UUID) -> (str, str):
    expires = datetime.utcnow() + timedelta(minutes=30000)
    payload = {"exp": expires, "sub": str(user_id)}
    return encode(payload, key=SECRET, algorithm=ALGORITHM)


def token_decode(token: str) -> dict:
    return decode(token, key=SECRET, algorithms=[ALGORITHM])
