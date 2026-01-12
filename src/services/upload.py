from fastapi import Depends

from db.repositories.accident import AccidentRepository
from services.base import BaseService


class UploadService(BaseService):
    def __init__(self, accident_repository: AccidentRepository = Depends()) -> None:
        self._accident_repository = accident_repository

    async def upload_accidents(self, file):
        await self._accident_repository.upload_accidents(accidents=[])
