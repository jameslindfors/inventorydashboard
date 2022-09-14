from http.client import HTTPException
from itertools import product
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
    '/get/collection/{collection_id}', response_model=Product_Pydantic, responses={404: {'model': HTTPNotFoundError}}, tags=['product', 'collection']
)
async def get_collection_by_id(collection_id: int):
    return "Get all by collection"

@router.post(
    '/create', response_model=Product_Pydantic, status_code=201, tags=['product']
)
async def create_products(product: ProductIn_Pydantic):
    product_obj = await Product.create(**product.dict(exclude_unset=True))
    return await Product_Pydantic.from_tortoise_orm(product_obj)

@router.post('/create/collection', status_code=201, tags=['product', 'collection'])
def create_collection():
    return "Create collection"

@router.put(
    '/update/{product_id}', response_model=Product_Pydantic, tags=['product']
)
async def update_product_by_id(product_id: int, product: ProductIn_Pydantic):
    await Product.filter(id=product_id).update(**product.dict(exclude_unset=True))
    return await Product_Pydantic.from_queryset_single(Product.get(id=product_id))

@router.put('/update/collection/{collection_id}', tags=['product', 'collection'])
def update_collection_by_id():
    return "Update collection by id"

@router.delete(
    '/delete/{product_id}', responses={404: {'model': HTTPNotFoundError}}, tags=['product']
)
async def delete_product_by_id(product_id: int):
    deleted = await Product.filter(id=product_id).delete()
    if not deleted: 
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return {"status": f"{product_id} deleted successfully"}

@router.delete('/delete/collection/{collection_id}', tags=['product', 'collection'])
def delete_collection_by_id():
    return "Delete collection by id"

# Product Utilities
@router.post('/upload', tags=['product', 'utilities'])
def upload_product_data():
    return "Upload product data"

@router.get('/download', tags=['product', 'utilities'])
def download_product_data():
    return "Download product data"