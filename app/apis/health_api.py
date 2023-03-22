from fastapi import APIRouter, Depends, status
from fastapi.responses import PlainTextResponse

from app.services.health_srv import HealthSrv

router = APIRouter(tags=["healthcheck"])

HEALTHY_RESPONSE = "Application is healthy"
UNHEALTHY_RESPONSE = "Application is unhealthy"


@router.get("/health", summary="Health check", status_code=status.HTTP_200_OK)
async def health(
    health_srv: HealthSrv = Depends(HealthSrv),
    response: PlainTextResponse = PlainTextResponse(),
) -> PlainTextResponse:
    if await health_srv.is_healthy():
        response.status_code = status.HTTP_200_OK
        response = HEALTHY_RESPONSE
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = UNHEALTHY_RESPONSE
    return response
