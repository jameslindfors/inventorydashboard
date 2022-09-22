"""API V1 Module"""
import os
from fastapi import APIRouter

from core.models.database import init_db
from core.config import settings
from .endpoints import (
    collection,
    inventory,
    product,
    util
)
router = APIRouter()

def register_v1(_app):
    """ Register API Routes with App

    Args:
        _app(): app instance
    """
    init_db(_app)

    product_enabled = os.getenv('PRODUCT_ENABLED', 'y')
    collection_enabled = os.getenv('COLLECTION_ENABLED', 'y')
    inventory_enabled = os.getenv('INVENTORY_ENABLED', 'y')
    utils_enabled = os.getenv('UTILS_ENABLED', 'y')

    if product_enabled == 'y':
        _app.include_router(product.router, prefix=f'/{settings.uri_prefix}/p')
    if collection_enabled == 'y':
        _app.include_router(collection.router, prefix=f'/{settings.uri_prefix}/c')
    if inventory_enabled == 'y':
        _app.include_router(inventory.router, prefix=f'/{settings.uri_prefix}/i')
    if utils_enabled == 'y':
        _app.include_router(util.router, prefix=f'/{settings.uri_prefix}/u')
