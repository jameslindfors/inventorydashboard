from fastapi import APIRouter

router = APIRouter()

@router.get('/get/{product_id}', tags=['product'])
def get_product_by_id():
    return 'Get product by id'

@router.get('/get/collection/{collection_id}', tags=['product', 'collection'])
def get_collection_by_id():
    return "Get all by collection"

@router.post('/create', status_code=201, tags=['product'])
def create_products():
    return "Create Products"

@router.post('/create/collection', status_code=201, tags=['product', 'collection'])
def create_collection():
    return "Create collection"

@router.put('/update/{product_id}', tags=['product'])
def update_product_by_id():
    return "Update product by id"

@router.put('/update/collection/{collection_id}', tags=['product', 'collection'])
def update_collection_by_id():
    return "Update collection by id"

@router.delete('/delete/{product_id}', tags=['product'])
def delete_product_by_id():
    return "Delete product by id"

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