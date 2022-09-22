"""Util Endpoint"""
from fastapi import APIRouter

router = APIRouter()

@router.post('/upload', tags=['utilities'])
def upload_product_data():
    """ Capture File to Parse
    - CSV, JSON

    Returns:
        str: return string
    """
    return "Upload data"

@router.get('/download', tags=['utilities'])
def download_product_data():
    """ Generate Product Data Download
    - CSV, PDF, HTML

    Returns:
        str: return string
    """
    return "Download data"
