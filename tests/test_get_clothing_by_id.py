
from backend.services.wardrobe_service import get_clothing_item_by_id


item = get_clothing_item_by_id(2)

if item:
    print("Clothing item found!")
    print("ID:", item.id)
    print("Category:", item.category)
    print("Main color:", item.color)
    print("Secondary colors:", item.secondary_colors)
    print("Style:", item.style)
    print("Pattern:", item.pattern)
    print("Seasons:", item.seasons)
    print("Weather suitability:", item.weather_suitability)
else:
    print("Clothing item not found.")
