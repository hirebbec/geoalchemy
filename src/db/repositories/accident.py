from typing import Sequence


from db.models import Accident
from db.repositories.base import BaseDatabaseRepository
from schemas.accident import CreateAccidentSchema, GetAccidentSchema
from sqlalchemy import insert, select
from geoalchemy2.shape import from_shape
from shapely.geometry import shape


class AccidentRepository(BaseDatabaseRepository):
    async def create_accident(self, accident: CreateAccidentSchema) -> None:
        query = insert(Accident).values(
            geometry=from_shape(shape(accident.geometry.model_dump()), srid=4326),
        )

        await self._session.execute(query)
        await self._session.flush()

    async def get_accident_by_id(self, id: int) -> GetAccidentSchema | None:
        query = select(Accident).where(Accident.id == id)
        result = await self._session.execute(query)

        accident = result.scalars().first()

        return GetAccidentSchema.model_validate(accident) if accident else None

    async def get_accidents(self) -> Sequence[GetAccidentSchema]:
        query = select(Accident).order_by(Accident.id)

        result = await self._session.execute(query)

        return [
            GetAccidentSchema.model_validate(accident)
            for accident in result.scalars().all()
        ]
