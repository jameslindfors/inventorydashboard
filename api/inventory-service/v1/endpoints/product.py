"""Product Endpoint"""
from http.client import HTTPException
from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from core.models.model import Collection, Product
from core.schemas.product import Product_Pydantic, ProductIn_Pydantic

router = APIRouter()

@router.get(
    '/get/{product_id}', response_model=Product_Pydantic,
    responses={404: {"model": HTTPNotFoundError}}, tags=['product']
)
async def get_product_by_id(product_id: int):
    """ Retrieve Singe Product by Id

    Args:
        product_id (int): id of the product

    Returns:
        Product: single product
    """
    return await Product_Pydantic.from_queryset_single(Product.get(id=product_id))

@router.get(
    '/get-all/', response_model=List[Product_Pydantic],
    responses={404: {'model': HTTPNotFoundError}}, tags= ['product']
)
async def get_all_products():
    """ Retrieve all Products

    Returns:
        dict: data
    """
    return await Product_Pydantic.from_queryset(Product.all())

@router.post(
    '/create/{collection_id}', response_model=Product_Pydantic,
    status_code=201, tags=['product']
)
async def create_products(collection_id: int, product: ProductIn_Pydantic):
    """ Create New Product from Data

    Args:
        collection_id (int): id of the collection product is member of
        product (ProductIn_Pydantic): data fields

    Returns:
        Product: single product
    """
    collection_obj = await Collection.get(id = collection_id)
    product_obj = await Product.create(**product.dict(exclude_unset=True),
                                    collection = collection_obj)
    return await Product_Pydantic.from_tortoise_orm(product_obj)

@router.put(
    '/update/{product_id}', response_model=Product_Pydantic, tags=['product']
)
async def update_product_by_id(product_id: int, product: ProductIn_Pydantic):
    """ Update Product Data Fields

    Args:
        product_id (int): id of product
        product (ProductIn_Pydantic): data fields

    Returns:
        Product: singe product
    """
    await Product.filter(id=product_id).update(**product.dict(exclude_unset=True))
    return await Product_Pydantic.from_queryset_single(Product.get(id=product_id))

@router.delete(
    '/delete/{product_id}', responses={404: {'model': HTTPNotFoundError}}, tags=['product']
)
async def delete_product_by_id(product_id: int):
    """ Delete Product

    Args:
        product_id (int): id of the product

    Raises:
        HTTPException: product id not valid

    Returns:
        dict: status
    """
    deleted = await Product.filter(id=product_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return {"status": f"{product_id} deleted successfully"}
