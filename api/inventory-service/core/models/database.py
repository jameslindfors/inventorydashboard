"""Database Module"""
from tortoise.contrib.fastapi import register_tortoise
from core.config import settings
from ..utils import generate_db_uri

def init_db(app):
    """ Registers Tortoise ORM
    - Connect API
    - Connect DB
    - Register Modules
    - Generate Schema
    Args:
        app: fastapi app instance
    """
    register_tortoise(
        app,
        db_url=generate_db_uri(
            user=settings.postgresql_username,
            password=settings.postgresql_password,
            database=settings.postgresql_database
            ),
        modules={'models': ['models.product_model']},
        generate_schemas=True,
        add_exception_handlers=True
    )
