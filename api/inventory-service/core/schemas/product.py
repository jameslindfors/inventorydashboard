"""Product Schema Module"""
from tortoise.contrib.pydantic import pydantic_model_creator
from core.models.model import Product

# Product Pydantic Models
Product_Pydantic = pydantic_model_creator(Product, name='Product')
ProductIn_Pydantic = pydantic_model_creator(Product, name='ProductIn', exclude_readonly=True)
