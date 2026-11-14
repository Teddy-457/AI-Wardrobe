
from backend.services.wardrobe_service import update_clothing_item


updated_item = update_clothing_item(
    2,  # Променяме ID от 1 на 2
    color="Blue",
    style="Sport",
    secondary_colors=["White", "Black"]
)
if updated_item:
    print("Clothing item updated successfully!")
    print("ID:", updated_item.id)
    print("Category:", updated_item.category)
    print("Main color:", updated_item.color)
    print("Secondary colors:", updated_item.secondary_colors)
    print("Style:", updated_item.style)
else:
    print("Clothing item not found.")
