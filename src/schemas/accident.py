from schemas.geometry import GeometryMixinSchema
from schemas.mixins import CreatedAtSchema, UpdatedAtSchema, IDSchema


class CreateAccidentSchema(GeometryMixinSchema):
    pass


class UpdateAccidentSchema(CreateAccidentSchema):
    pass


class GetAccidentSchema(
    UpdateAccidentSchema, IDSchema, CreatedAtSchema, UpdatedAtSchema
):
    pass
