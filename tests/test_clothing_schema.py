from pydantic import ValidationError
from backend.schemas.clothing_schema import ClothingItemSchema


clothing_data = {
    "image_path": "storage/clothing_images/test_tshirt.jpg",
    "category": "T-shirt",
    "color": "Black",
    "secondary_colors": ["White", "Gray"],
    "style": "Casual",
    "pattern": "Plain",
    "seasons": ["Spring", "Summer", "Autumn"],
    "weather_suitability": ["Warm", "Dry"]
}


clothing_item = ClothingItemSchema(**clothing_data)

print("Validation successful!")
print(clothing_item.model_dump())


from pydantic import ValidationError


invalid_data = {
    "image_path": "storage/clothing_images/test.jpg",
    "category": "T-shirt",
    "color": "Black",
    "secondary_colors": "White",
    "seasons": ["Summer"]
}

try:
    ClothingItemSchema(**invalid_data)

except ValidationError as error:
    print("\nInvalid data rejected successfully!")
    print(error)

# Test: празна категория трябва да бъде отхвърлена

empty_category_data = {
    "image_path": "storage/clothing_images/test.jpg",
    "category": "",
    "color": "Black"
}

try:
    ClothingItemSchema(**empty_category_data)

except ValidationError as error:
    print("\nEmpty category rejected successfully!")
    print(error)


whitespace_data = {
    "image_path": " storage/clothing_images/test.jpg ",
    "category": " T-shirt ",
    "color": " Black "
}

item = ClothingItemSchema(**whitespace_data)

print("\nWhitespace test:")
print(f"Category: '{item.category}'")
print(f"Color: '{item.color}'")

extra_field_data = {
    "image_path": "storage/clothing_images/test.jpg",
    "category": "T-shirt",
    "color": "Black",
    "material": "Cotton"
}

try:
    ClothingItemSchema(**extra_field_data)

except ValidationError as error:
    print("\nExtra field rejected successfully!")
    print(error)

