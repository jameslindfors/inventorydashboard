"""Collection Schema Module"""
from tortoise.contrib.pydantic import pydantic_model_creator
from core.models.collection import Collection

# Collection Pydantic Models
Collection_Pydantic = pydantic_model_creator(Collection, name="Collection")
CollectionIn_Pydantic = pydantic_model_creator(Collection, name="Collection", exclude_readonly=True)
