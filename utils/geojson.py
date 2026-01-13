from typing import Any, Sequence

from schemas.geojson import FeatureSchema, GeojsonSchema
from schemas.geometry import GeometryMixinSchema


def get_nested_attr(obj, attr_path: str) -> Any:
    for attr in attr_path.split("."):
        obj = getattr(obj, attr)
    return obj


def process_properties(schema, props: list[str]) -> dict[str, Any]:
    result = {}
    for prop in props:
        key = prop.split(".")[-1]
        try:
            result[key] = get_nested_attr(schema, prop)
        except AttributeError:
            result[key] = None
    return result


def get_geojsons_from_schemas(
    schemas: Sequence[GeometryMixinSchema], properties: list[str] | None = None
) -> GeojsonSchema:
    return GeojsonSchema(
        features=[
            FeatureSchema(
                geometry=schema.geometry,
                properties=process_properties(schema, properties)
                if properties
                else schema.model_dump(),
            )
            for schema in schemas
            if schema.geometry
        ]
    )
