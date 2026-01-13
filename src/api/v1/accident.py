from typing import Sequence

from fastapi import APIRouter, Depends
from starlette import status

from schemas.accident import CreateAccidentSchema, GetAccidentSchema
from schemas.geojson import GeojsonSchema
from services.accident import AccidentService

router = APIRouter(prefix="/accidents", tags=["Accidents"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_accident(
    accident: CreateAccidentSchema, accident_service: AccidentService = Depends()
) -> None:
    await accident_service.create_accidents(accident=accident)


@router.get("/geojson", status_code=status.HTTP_200_OK, response_model=GeojsonSchema)
async def get_accident_geojson(accident_service: AccidentService = Depends()):
    return await accident_service.get_accident_geojson()


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=Sequence[GetAccidentSchema]
)
async def get_accidents(accident_service: AccidentService = Depends()):
    return await accident_service.get_accidents()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=GetAccidentSchema)
async def get_accident_by_id(
    id: int, accident_service: AccidentService = Depends()
) -> GetAccidentSchema | None:
    return await accident_service.get_accident_by_id(id=id)
