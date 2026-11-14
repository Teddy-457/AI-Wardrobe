from typing import Literal

from pydantic import BaseModel, Field


class ClothingAttributes(BaseModel):
    category: str = Field(max_length=64)
    main_color: str = Field(max_length=32)
    secondary_colors: list[str] = Field(default_factory=list, max_length=4)
    pattern: str = Field(max_length=64)
    style: str = Field(max_length=64)
    seasons: list[Literal["spring", "summer", "autumn", "winter"]] = Field(
        max_length=4
    )
    weather_suitability: list[str] = Field(default_factory=list, max_length=6)
