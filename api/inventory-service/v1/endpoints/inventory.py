"""Inventory Endpoint"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/inventory", tags=['inventory'])
async def inventory_get(skip = 0, limit = 5):
    """ Get Inventory

    Args:
        skip (int, optional): number to skip. Defaults to 0.
        limit (int, optional): limit to retrieve. Defaults to 5.

    Returns:
        dict: status
    """
    return {"inventory_status": 1, "args": {"skip": skip, "limit": limit}}

@router.put("/{inventory_id}", tags=['inventory'])
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
