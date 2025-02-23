from typing import List

from pydantic import BaseModel, Field

from ._base import Coordinates, GeoJSONModel, LineStringFieldType


class LineStringModel(GeoJSONModel):
    type: LineStringFieldType
    coordinates: List[Coordinates] = Field(..., min_length=2)
