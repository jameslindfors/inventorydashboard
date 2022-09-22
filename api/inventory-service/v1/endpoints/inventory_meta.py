"""Inventory Endpoint"""
from fastapi import APIRouter
import datetime

from core.models.inventory_meta import InventoryMeta
from core.schemas.inventory_meta import InventoryMeta_Pydantic, InventoryMetaIn_Pydantic

router = APIRouter()

@router.get("/inventory_meta", tags=['inventory'])
async def inventory_get(skip = 0, limit = 5):
    """ Get Inventory

    Args:
        skip (int, optional): number to skip. Defaults to 0.
        limit (int, optional): limit to retrieve. Defaults to 5.

    Returns:
        dict: status
    """
    inventory_obj = await InventoryMeta_Pydantic.from_queryset_single(InventoryMeta.all())
    return {"data": inventory_obj, "args": {"skip": skip, "limit": limit}}

@router.put("/{inventory_id}", response_model=InventoryMeta_Pydantic, tags=['inventory'])
async def inventory_update(inventory_id: int):
    """ Update Inventory Fields

    Args:
        inventory_id (int): id of the inventory

    Returns:
        dict: status
    """
    return {"inventory_id": inventory_id, "amount": 10}

@router.delete("/clear", tags=['inventory'])
async def inventory_clear():
    """ Delete all items in inventory

    Returns:
        dict: status
    """
    return {"status": "cleared"}
