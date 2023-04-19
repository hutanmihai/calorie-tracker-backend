from pydantic import BaseModel


class ApiError(BaseModel):
    status_code: int
    description: str

    class Config:
        schema_extra = {
            "example": {
                "status_code": "<error code>",
                "description": "<error description>",
            }
        }


class AuthError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "detail": "<error description>",
            }
        }
