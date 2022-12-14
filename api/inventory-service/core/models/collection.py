"""Collection Model Module"""
from tortoise import fields
from tortoise.models import Model

class Collection(Model):
    """ Tortoise ORM Collection Model

    Args:
        Model (_type_): ORM base model
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    description = fields.CharField(max_length=500)
