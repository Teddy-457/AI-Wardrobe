
import os

from backend.services.image_service import (
    validate_image,
    save_image
)


image_path = "storage/clothing_images/test_tshirt.jpg"


try:
    result = validate_image(image_path)
    print("Image validation successful:", result)

    saved_path = save_image(image_path)

    print("Image saved successfully!")
    print("Saved path:", saved_path)
    print("File exists:", os.path.isfile(saved_path))

except (FileNotFoundError, ValueError) as error:
    print("Image processing failed:", error)
