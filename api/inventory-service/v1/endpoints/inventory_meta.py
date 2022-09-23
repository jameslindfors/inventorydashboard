"""Inventory Endpoint"""
from fastapi import APIRouter
import datetime

from core.models.inventory_meta import InventoryMeta
from core.schemas.inventory_meta import InventoryMeta_Pydantic
from v1.services.inventory_meta import init_inventory_metadata, update_inventory_metadata

router = APIRouter()

@router.get("/inventory_meta", tags=['inventory'])
async def inventory_get(skip = 0, limit = 5):
    """ Get Inventory

    Returns:
        InventoryMeta: single instance
    """
    return await InventoryMeta_Pydantic.from_queryset_single(InventoryMeta.first())

@router.post("/inventory_meta", tags=['inventory'])
async def inventory_init():
    return await init_inventory_metadata()

@router.put("/inventory_meta", tags=['inventory'])
async def inventory_update():
    """ Update Inventory Fields
    """
    return await update_inventory_metadata()
