from db.repositories.base import BaseDatabaseRepository


class AccidentRepository(BaseDatabaseRepository):
    async def create_accident(self, accident: CreateAccidentSchema) -> None:
        pass
