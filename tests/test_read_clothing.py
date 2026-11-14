
from backend.services.wardrobe_service import get_all_clothing_items


clothing_items = get_all_clothing_items()

if clothing_items:
    for item in clothing_items:
        print("----------------------")
        print("ID:", item.id)
        print("Category:", item.category)
        print("Main color:", item.color)
        print("Secondary colors:", item.secondary_colors)
        print("Style:", item.style)
        print("Pattern:", item.pattern)
        print("Seasons:", item.seasons)
        print("Weather suitability:", item.weather_suitability)
else:
    print("The wardrobe is empty.")
