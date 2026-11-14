from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func

from backend.database.db import Base


class ClothingItem(Base):

    __tablename__ = "ClothingItems"

    id = Column(Integer, primary_key=True, index=True)

    image_path = Column(String(500), nullable=False)

    category = Column(String(100), nullable=False)

    # Основен цвят
    color = Column(String(50), nullable=False)

    # Допълнителни цветове
    secondary_colors = Column(JSON, nullable=True)

    style = Column(String(100), nullable=True)

    pattern = Column(String(100), nullable=True)

    seasons = Column(JSON, nullable=True)

    weather_suitability = Column(JSON, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )