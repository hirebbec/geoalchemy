from typing import Any

from schemas.base import BaseSchema


class GeometrySchema(BaseSchema):
    type: str
    coordinates: Any
