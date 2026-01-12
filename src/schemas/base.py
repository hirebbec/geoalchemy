from datetime import datetime

from pydantic import BaseModel, ConfigDict

from core.config import settings
from schemas.mixins import CreatedAtSchema, UpdatedAtSchema


class BaseSchema(BaseModel, CreatedAtSchema, UpdatedAtSchema):
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda dt: dt.astimezone(tz=settings().TIME_ZONE),
        },
    )
