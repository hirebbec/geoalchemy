from typing import Sequence

from fastapi import Depends

from db.repositories.accident import AccidentRepository
from schemas.accident import CreateAccidentSchema, GetAccidentSchema
from schemas.geojson import GeojsonSchema
from services.base import BaseService
from utils.geojson import get_geojsons_from_schemas


class AccidentService(BaseService):
    def __init__(self, accident_repository: AccidentRepository = Depends()) -> None:
        self._accident_repository = accident_repository

    async def create_accidents(self, accident: CreateAccidentSchema) -> None:
        await self._accident_repository.create_accident(accident=accident)

    async def get_accident_by_id(self, id: int) -> GetAccidentSchema | None:
        return await self._accident_repository.get_accident_by_id(id=id)

    async def get_accidents(self) -> Sequence[GetAccidentSchema]:
        return await self._accident_repository.get_accidents()

    async def get_accident_geojson(self) -> GeojsonSchema:
        return get_geojsons_from_schemas(
            schemas=await self._accident_repository.get_accidents(),
            properties=["id", "created_at"],
        )
