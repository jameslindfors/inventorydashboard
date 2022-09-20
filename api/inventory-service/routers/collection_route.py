from http.client import HTTPException
from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from models.product_model import Product, Collection, CollectionIn_Pydantic, Collection_Pydantic

router = APIRouter()

@router.get(
    '/get/collection/{collection_id}', response_model=Collection_Pydantic, responses={404: {'model': HTTPNotFoundError}}, tags=['collection']
) 
async def get_collection_by_id(collection_id: int):
    return await Collection_Pydantic.from_queryset_single(Collection.get(id=collection_id))

@router.get(
    '/get-all/collection', response_model=List[Collection_Pydantic], responses={404: {'model': HTTPNotFoundError}}, tags=['collection']
)
async def get_all_collections():
    collection = await Collection.all()
    
    for x in collection:
        products = await Product.all().filter(collection_id=x.id)
        for y in products:
            print(y.name)
            
    return await Collection_Pydantic.from_queryset(Collection.all())

@router.post('/create/collection', response_model=Collection_Pydantic, status_code=201, tags= ['collection']
)
async def create_collection(collection: CollectionIn_Pydantic):
    collection_obj = await Collection.create(**collection.dict(exclude_unset=True))
    return await Collection_Pydantic.from_tortoise_orm(collection_obj)

@router.put('/update/collection/{collection_id}', response_model=Collection_Pydantic, tags=['collection']
)
async def update_collection_by_id(collection_id: int, collection: CollectionIn_Pydantic):
    await Collection.filter(id=collection_id).update(**collection.dict(exclude_unset=True))
    return await Collection_Pydantic.from_queryset_single(Collection.get(id=collection_id))

@router.delete('/delete/collection/{collection_id}', responses={404: {'model': HTTPNotFoundError}},tags=['collection']
)
async def delete_collection_by_id(collection_id: int):
    deleted = await Collection.filter(id=collection_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Collection {collection_id} not found")
    return {"status": f"{collection_id} deleted successfully"}