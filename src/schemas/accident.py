from schemas.geometry import GeometryMixinSchema
from schemas.mixins import CreatedAtSchema, UpdatedAtSchema


class CreateAccidentSchema(GeometryMixinSchema):
    pass

class UpdateAccidentSchema(CreateAccidentSchema):
    pass

class GetAccidentSchema(UpdateAccidentSchema, CreatedAtSchema, UpdatedAtSchema):
    pass