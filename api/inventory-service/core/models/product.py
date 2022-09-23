"""Product Model Module"""
from tortoise import fields
from tortoise.models import Model

class Product(Model):
    """ Tortoise ORM Product Model

    Args:
        Model (_type_): ORM base model
    """

    id = fields.IntField(pk=True)

    name = fields.CharField(150)
    description = fields.CharField(500)
    image = fields.CharField(50)

    price = fields.FloatField()
    tax_rate = fields.FloatField()
    shipping_rate = fields.FloatField()
    currency = fields.CharField(50)

    total_units = fields.IntField()
    current_units = fields.IntField()

    sale = fields.BooleanField()
    sale_percent = fields.FloatField()

    collection = fields.ForeignKeyField('models.Collection', related_name='products')
