from .database import session, Base


def add_new_obj_to_db(obj: Base) -> None:
    """Add new object to the database."""
    session.add(obj)
    session.commit()
