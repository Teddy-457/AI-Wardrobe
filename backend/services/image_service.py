
import os


ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}


def validate_image(image_path):

    if not os.path.isfile(image_path):
        raise FileNotFoundError(
            f"Image file does not exist: {image_path}"
        )

    extension = os.path.splitext(image_path)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported image format: {extension}"
        )

    return True


import shutil
import uuid


def save_image(image_path):

    # Проверяваме дали снимката е валидна
    validate_image(image_path)

    # Определяме главната директория на проекта
    project_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    # Директория за съхраняване на снимките
    storage_dir = os.path.join(
        project_dir,
        "storage",
        "clothing_images"
    )

    # Създаваме директорията, ако не съществува
    os.makedirs(storage_dir, exist_ok=True)

    # Запазваме оригиналното разширение
    extension = os.path.splitext(image_path)[1].lower()

    # Генерираме уникално име
    filename = str(uuid.uuid4()) + extension

    destination = os.path.join(storage_dir, filename)

    # Копираме снимката
    shutil.copy2(image_path, destination)

    # Връщаме относителния път
    relative_path = os.path.relpath(
        destination,
        project_dir
    )

    return relative_path
