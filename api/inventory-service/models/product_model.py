from time import timezone
from tortoise import fields
from tortoise.models import Model

from tortoise.contrib.pydantic import pydantic_model_creator

# Tortoise ORM Model
class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50, unique=True)

# Pydantic Model
Product_Pydantic = pydantic_model_creator(Product, name='Product')
ProductIn_Pydantic = pydantic_model_creator(Product, name='ProductIn', exclude_readonly=True)