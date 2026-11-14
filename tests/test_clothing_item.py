
from backend.services.wardrobe_service import add_clothing_item


new_item = add_clothing_item(
    image_path="storage/clothing_images/test_tshirt.jpg",
    category="T-shirt",
    color="Black",
    secondary_colors=["White", "Gray"],
    style="Casual",
    pattern="Plain",
    seasons=["Spring", "Summer", "Autumn"],
    weather_suitability=["Warm", "Dry"]
)

print("Clothing item added successfully!")
print("ID:", new_item.id)
print("Category:", new_item.category)
print("Main color:", new_item.color)
print("Secondary colors:", new_item.secondary_colors)
print("Seasons:", new_item.seasons)
print("Weather suitability:", new_item.weather_suitability)

from pydantic import ValidationError


try:
    add_clothing_item(
        image_path="storage/clothing_images/test.jpg",
        category="",
        color="Black"
    )

except ValidationError as error:
    print("\nInvalid clothing item rejected!")
    print(error)
