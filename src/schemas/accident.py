from schemas.base import BaseSchema
from schemas.geometry import GeometrySchema


class CreateAccidentSchema(BaseSchema):
    geometry: GeometrySchema
