from http.client import HTTPException
from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from models.product_model import Product, ProductIn_Pydantic, Product_Pydantic

router = APIRouter()

@router.get(
    '/get/{product_id}', response_model=Product_Pydantic, responses={404: {"model": HTTPNotFoundError}}, tags=['product']
)
async def get_product_by_id(product_id: int):
    return await Product_Pydantic.from_queryset_single(Product.get(id=product_id))

@router.get(
    '/get-all/', response_model=List[Product_Pydantic], responses={404: {'model': HTTPNotFoundError}}, tags= ['product']
)
async def get_all_products():
    return await Product_Pydantic.from_queryset(Product.all())

@router.post(
    '/create', response_model=Product_Pydantic, status_code=201, tags=['product']
)
async def create_products(product: ProductIn_Pydantic):
    product_obj = await Product.create(**product.dict(exclude_unset=True))
    return await Product_Pydantic.from_tortoise_orm(product_obj)

@router.put(
    '/update/{product_id}', response_model=Product_Pydantic, tags=['product']
)
async def update_product_by_id(product_id: int, product: ProductIn_Pydantic):
    await Product.filter(id=product_id).update(**product.dict(exclude_unset=True))
    return await Product_Pydantic.from_queryset_single(Product.get(id=product_id))

@router.delete(
    '/delete/{product_id}', responses={404: {'model': HTTPNotFoundError}}, tags=['product']
)
async def delete_product_by_id(product_id: int):
    deleted = await Product.filter(id=product_id).delete()
    if not deleted: 
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return {"status": f"{product_id} deleted successfully"}