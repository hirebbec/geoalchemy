from typing import Any, Sequence

from schemas.base import BaseSchema
from schemas.geometry import GeometrySchema


class FeatureSchema(BaseSchema):
    type: str = "Feature"
    geometry: GeometrySchema
    properties: dict[str, Any]


class GeojsonSchema(BaseSchema):
    type: str = "FeatureCollection"
    features: Sequence[FeatureSchema]
