from tortoise import fields
from tortoise.models import Model

from tortoise.contrib.pydantic import pydantic_model_creator

# Tortoise ORM Model
class Product(Model):
    id = fields.IntField(pk=True)
    
    name = fields.CharField(50, unique=True)
    description = fields.CharField(50)
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

# Pydantic Model
Product_Pydantic = pydantic_model_creator(Product, name='Product')
ProductIn_Pydantic = pydantic_model_creator(Product, name='ProductIn', exclude_readonly=True)

class Collection(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    description = fields.CharField(max_length=100)
    
    
Collection_Pydantic = pydantic_model_creator(Collection, name="Collection")
CollectionIn_Pydantic = pydantic_model_creator(Collection, name="Collection", exclude_readonly=True)
