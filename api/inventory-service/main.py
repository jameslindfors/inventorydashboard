from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import product_route, inventory_route, collection_route, util_route
from db import database
from config import settings
import os

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, openapi_url=f"/{settings.URI_PREFIX}/openapi.json", docs_url=f"/{settings.URI_PREFIX}/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.on_event("startup")
async def startup():
    database.init_db(app)

product_enabled = os.getenv('PRODUCT_ENABLED', 'y')
collection_enabled = os.getenv('COLLECTION_ENABLED', 'y')
inventory_enabled = os.getenv('INVENTORY_ENABLED', 'y') 
utils_enabled = os.getenv('UTILS_ENABLED', 'y')


if product_enabled == 'y':
    app.include_router(product_route.router, prefix=f'/{settings.URI_PREFIX}/p')
if collection_enabled == 'y': 
    app.include_router(collection_route.router, prefix=f'/{settings.URI_PREFIX}/c')
if inventory_enabled == 'y':
    app.include_router(inventory_route.router, prefix=f'/{settings.URI_PREFIX}/i')
if utils_enabled == 'y':
    app.include_router(util_route.router, prefix=f'/{settings.URI_PREFIX}/u')