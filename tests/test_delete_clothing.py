
from backend.services.wardrobe_service import delete_clothing_item


deleted = delete_clothing_item(2)

if deleted:
    print("Clothing item deleted successfully!")
else:
    print("Clothing item not found.")
