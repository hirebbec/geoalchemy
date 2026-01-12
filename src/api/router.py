from fastapi import APIRouter

from core.config import settings
from api.v1.road import router as road_router
from api.v1.accident import router as accident_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(road_router)
v1_router.include_router(accident_router)

project_router = APIRouter(prefix=f"/{settings().PROJECT_NAME}")
project_router.include_router(v1_router)

api_router = APIRouter(prefix="/api")
api_router.include_router(project_router)
