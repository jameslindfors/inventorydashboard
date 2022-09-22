"""Inventory Meta Mdoel Module"""
from tortoise import fields
from tortoise.models import Model

class InventoryMeta(Model):
    """ Tortoise ORM Inventory Metadata Model

    Args:
        Model (_type_): ORM base model
    """

    created_at = fields.DateField(pk=True)
    updated_at = fields.DatetimeField(auto_now=True)