from fastapi import Depends

from db.repositories.accident import AccidentRepository
from schemas.accident import CreateAccidentSchema, GetAccidentSchema
from services.base import BaseService


class AccidentService(BaseService):
    def __init__(self, accident_repository: AccidentRepository = Depends()) -> None:
        self._accident_repository = accident_repository

    async def create_accidents(self, accident: CreateAccidentSchema) -> None:
        await self._accident_repository.create_accident(accident=accident)

    async def get_accident_by_id(self, id: int) -> GetAccidentSchema:
        return await self._accident_repository.get_accident_by_id(id=id)
