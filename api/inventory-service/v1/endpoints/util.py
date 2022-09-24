"""Util Endpoint"""
import pandas as pd
from fastapi import APIRouter, File, UploadFile

from core.models.collection import Collection

router = APIRouter()

@router.post('/upload', tags=['utilities'])
async def upload_product_data(file: UploadFile = File(...)):
    """ Capture File to Parse
    - CSV, JSON

    Returns:
        str: return string
    """
    df = pd.read_csv(file.file)
    n = df.to_numpy()

    status = "Success"
    data = []
    for x in n:
        data.append(await Collection.create(id=x[0], name=x[1], description=x[2]))
        
    response = {
        'status': status,
        'added': data.__len__(),
        'data': data,
        'csv': df.to_csv()
    }
    return response

@router.get('/download', tags=['utilities'])
def download_product_data():
    """ Generate Product Data Download
    - CSV, PDF, HTML

    Returns:
        str: return string
    """
    return "Download data"
