from tortoise.contrib.fastapi import register_tortoise
from .utils import generate_db_uri
from config import settings

def init_db(app):
    register_tortoise(
        app,
        db_url=generate_db_uri(
            user=settings.POSTGRESQL_USERNAME,
            password=settings.POSTGRESQL_PASSWORD,
            db=settings.POSTGRESQL_DATABASE
            ),
        modules={'models': ['models.product_model']},
        generate_schemas=True,
        add_exception_handlers=True 
    )