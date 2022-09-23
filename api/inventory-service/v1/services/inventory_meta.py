"""Inventory Meta Service"""
import datetime

from core.models.inventory_meta import InventoryMeta

async def init_inventory_metadata():
    await InventoryMeta.create(created_at=datetime.date.today(), updated_at=datetime.datetime.utcnow())
    
async def update_inventory_metadata():
    entry = await InventoryMeta.first()
    await entry.save()
    