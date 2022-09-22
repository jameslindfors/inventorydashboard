"""Collection Endpoint"""
from http.client import HTTPException
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from core.models.product import Product
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
async def get_all_collections():
    """ Retrieve all Collections

    Returns:
        dict: data
    """
    res = await Collection.all()
    # collection_obj = await Collection_Pydantic.from_queryset(Collection.all())
    idx = 0
    for item in res:
        res[idx] = dict(item, **{'products': await Product.all().filter(collection_id=item.id)})
        idx = idx + 1
        # x.append(await Product.all().filter(collection_id=x.id))
    return {'data': res}

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

@router.put('/update/collection/{collection_id}',response_model=Collection_Pydantic,
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
