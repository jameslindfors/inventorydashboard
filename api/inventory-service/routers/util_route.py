from http.client import HTTPException
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()

@router.post('/upload', tags=['utilities'])
def upload_product_data():
    return "Upload data"

@router.get('/download', tags=['utilities'])
def download_product_data():
    return "Download data"