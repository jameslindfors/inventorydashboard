"""Inventory Meta Schema Module"""
from tortoise.contrib.pydantic import pydantic_model_creator
from core.models.inventory_meta import InventoryMeta

# Inventory Meta Pydantic Models
InventoryMeta_Pydantic = pydantic_model_creator(InventoryMeta, name="Inventory Meta")
InventoryMetaIn_Pydantic = pydantic_model_creator(InventoryMeta, name="Inventory Meta", exclude_readonly=True)
