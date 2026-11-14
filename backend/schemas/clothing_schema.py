
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class ClothingItemSchema(BaseModel):

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )

    image_path: str = Field(min_length=1)
    category: str = Field(min_length=1)
    color: str = Field(min_length=1)

    secondary_colors: Optional[list[str]] = None

    style: Optional[str] = None
    pattern: Optional[str] = None

    seasons: Optional[list[str]] = None
    weather_suitability: Optional[list[str]] = None
