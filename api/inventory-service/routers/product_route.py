from fastapi import APIRouter

router = APIRouter()


@router.get('/', tags=['product'])
def product():
    return 'Product API is running'

@router.post("/create", status_code=201, tags=['product'])
async def product_create():
    return 

@router.get("/{product_id}", tags=['product'])
async def product_get(product_id):
    return {"product_id": product_id}

@router.put("/{product_id}", tags=['product'])
async def product_update(product_id):
    return {"product_status": "updated", "id": product_id}

@router.delete("/{product_id}", tags=['product'])
async def product_delete(product_id):
    return {"product_status": "deleted", "id": product_id} 