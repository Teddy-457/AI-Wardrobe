from backend.schemas.clothing_schema import ClothingItemSchema
from backend.database.db import SessionLocal
from backend.database.models import ClothingItem


def add_clothing_item(
    image_path,
    category,
    color,
    secondary_colors=None,
    style=None,
    pattern=None,
    seasons=None,
    weather_suitability=None
):

    clothing_data = ClothingItemSchema(
        image_path=image_path,
        category=category,
        color=color,
        secondary_colors=secondary_colors,
        style=style,
        pattern=pattern,
        seasons=seasons,
        weather_suitability=weather_suitability
    )
    db = SessionLocal()

    try:
        new_item = ClothingItem(
            **clothing_data.model_dump()
        )

        db.add(new_item)
        db.commit()
        db.refresh(new_item)

        return new_item


    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

def get_all_clothing_items():
    db = SessionLocal()

    try:
        return db.query(ClothingItem).all()

    finally:
        db.close()


def get_clothing_item_by_id(item_id):
    db = SessionLocal()

    try:
        return db.query(ClothingItem).filter(
            ClothingItem.id == item_id
        ).first()

    finally:
        db.close()


def update_clothing_item(item_id, **updated_fields):
    db = SessionLocal()

    try:
        item = db.query(ClothingItem).filter(
            ClothingItem.id == item_id
        ).first()

        if item is None:
            return None

        for field, value in updated_fields.items():
            if hasattr(item, field):
                setattr(item, field, value)

        db.commit()
        db.refresh(item)

        return item

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def delete_clothing_item(item_id):
    db = SessionLocal()

    try:
        item = db.query(ClothingItem).filter(
            ClothingItem.id == item_id
        ).first()

        if item is None:
            return False

        db.delete(item)
        db.commit()

        return True

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
