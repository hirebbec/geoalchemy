import json
from typing import Any

from geoalchemy2 import WKBElement
from geoalchemy2.shape import to_shape
from pydantic import field_validator
from shapely import to_geojson

from schemas.base import BaseSchema


class GeometrySchema(BaseSchema):
    type: str
    coordinates: Any


class GeometryMixinSchema(BaseSchema):
    geometry: GeometrySchema

    @field_validator("geometry", mode="before")
    @classmethod
    def validate_geometry(cls, value) -> dict[str, Any]:
        if isinstance(value, WKBElement):
            geom = to_shape(value)
            return json.loads(to_geojson(geom))
        return value
