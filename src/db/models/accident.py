from geoalchemy2 import Geometry
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import IDMixin


class Accident(BaseModel, IDMixin):
    __tablename__ = "accidents"

    geometry: Mapped[Geometry] = mapped_column(
        Geometry("POINT", srid=4326), nullable=False
    )
