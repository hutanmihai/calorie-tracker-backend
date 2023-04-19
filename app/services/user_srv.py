from uuid import UUID

from fastapi import Depends

from app.models import User
from app.repositories.errors import EntityNotFound, EntityNotUnique
from app.repositories.user_repo import UserRepository
from app.services.abstract_srv import AbstractService
from app.services.errors import UserAlreadyExists, UserNotFound


class UserSrv(AbstractService):
    def __init__(self, repo: UserRepository = Depends(UserRepository)):
        super().__init__(repo)

    # Get user by id
    async def get_user(self, user_id: UUID) -> User:
        try:
            return await self._repository.get(User, user_id)
        except EntityNotFound:
            raise UserNotFound()

    # Create new user in the database
    async def new_user(self, g_id: str, email: str, name: str, picture: str) -> User:
        instance = User(g_id=g_id, email=email, name=name, picture=picture)
        try:
            return await self._repository.create(instance)
        except EntityNotUnique:
            raise UserAlreadyExists()

    # Get user by email
    async def get_user_by_email(self, email: str) -> User:
        try:
            return await self._repository.get_by_email(email)
        except EntityNotFound:
            raise UserNotFound()
