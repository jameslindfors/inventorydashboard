"""Collection Endpoint"""
from http.client import HTTPException
from typing import List, Union
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from core.models.product import Product
from core.schemas.product import Product_Pydantic
from core.models.collection import Collection
from core.schemas.collection import Collection_Pydantic, CollectionIn_Pydantic

router = APIRouter()

@router.get(
    '/get/collection/{collection_id}', response_model=Collection_Pydantic,
    responses={404: {'model': HTTPNotFoundError}}, tags=['collection']
)
async def get_collection_by_id(collection_id: int):
    """ Retrieve Single Collection by Id

    Args:
        collection_id (int): id of the collection

    Returns:
        Collection: single collection
    """
    return await Collection_Pydantic.from_queryset_single(Collection.get(id=collection_id))

@router.get(
    '/get-all/collection', responses={404: {'model': HTTPNotFoundError}}, tags=['collection']
)
async def get_all_collections(c_offset: int = 0, c_limit: Union[int, None] = None, 
                            extended: bool = False, 
                            p_offset: int = 0, p_limit: Union[int, None] = None):
    """ Retrieve all Collections

    Returns:
        List: collection and product data
    """
    if not extended:
        if c_limit:
            return await Collection_Pydantic.from_queryset(Collection.all().offset(c_offset).limit(c_limit))
        return await Collection_Pydantic.from_queryset(Collection.all().offset(c_offset))
    else:
        if c_limit:
            collection_obj = await Collection_Pydantic.from_queryset(Collection.all().offset(c_offset).limit(c_limit))
        else:
            collection_obj = await Collection_Pydantic.from_queryset(Collection.all().offset(c_offset))
        
        collection_list: List = []
        
        for collection in collection_obj:
            if p_limit:
                product_obj = await Product_Pydantic.from_queryset(Product.filter(collection_id=collection.id).offset(p_offset).limit(p_limit))
            else:
                product_obj = await Product_Pydantic.from_queryset(Product.filter(collection_id=collection.id).offset(p_offset))
            collection_list.append(dict(collection, **{'products': product_obj}))
            
        return collection_list

@router.post('/create/collection', response_model=Collection_Pydantic,
            status_code=201, tags= ['collection']
)
async def create_collection(collection: CollectionIn_Pydantic):
    """ Create New Collection from Data

    Args:
        collection (CollectionIn_Pydantic): data fields

    Returns:
        Collection: single collection
    """
    collection_obj = await Collection.create(**collection.dict(exclude_unset=True))
    return await Collection_Pydantic.from_tortoise_orm(collection_obj)

@router.put('/update/collection/{collection_id}', response_model=Collection_Pydantic,
            tags=['collection']
)
async def update_collection_by_id(collection_id: int, collection: CollectionIn_Pydantic):
    """ Update Collection Data Fields

    Args:
        collection_id (int): id of collection
        collection (CollectionIn_Pydantic): data fields

    Returns:
        Collection: single collection
    """
    await Collection.filter(id=collection_id).update(**collection.dict(exclude_unset=True))
    return await Collection_Pydantic.from_queryset_single(Collection.get(id=collection_id))

@router.delete('/delete/collection/{collection_id}',
            responses={404: {'model': HTTPNotFoundError}},tags=['collection']
)
async def delete_collection_by_id(collection_id: int):
    """ Delete Collection

    Args:
        collection_id (int): id of collection

    Raises:
        HTTPException: collection id not valid

    Returns:
        dict: status
    """
    deleted = await Collection.filter(id=collection_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Collection {collection_id} not found")
    return {"status": f"{collection_id} deleted successfully"}
