"""Pydantic models for structured clothing attributes."""

from typing import Literal

from pydantic import BaseModel, Field


# Pydantic models expose fields rather than public methods.
class ClothingAttributes(BaseModel):  # pylint: disable=too-few-public-methods
    """Describe the attributes extracted from a clothing image."""
    category: str = Field(max_length=64)
    main_color: str = Field(max_length=32)
    secondary_colors: list[str] = Field(default_factory=list, max_length=4)
    pattern: str = Field(max_length=64)
    style: str = Field(max_length=64)
    seasons: list[Literal["spring", "summer", "autumn", "winter"]] = Field(
        max_length=4
    )
    weather_suitability: list[str] = Field(default_factory=list, max_length=6)
