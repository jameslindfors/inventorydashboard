from tortoise.contrib.fastapi import register_tortoise

def init_db(app):
    register_tortoise(
    app,
    db_url='asyncpg://postgres:password@dev.localhost:5432',
    modules={'models': ['models.product_model']},
    generate_schemas=True,
    add_exception_handlers=True
)