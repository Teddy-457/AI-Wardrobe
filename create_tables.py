from backend.database.db import engine, Base
from backend.database.models import ClothingItem

# Създаване на таблиците, описани в моделите
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")