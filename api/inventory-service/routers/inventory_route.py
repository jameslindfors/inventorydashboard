from fastapi import APIRouter

router = APIRouter()


@router.get('/', tags=['inventory'])
def inventory():
    return 'Inventory API is running'

@router.get("/inventory", tags=['inventory'])
async def inventory_get(skip = 0, limit = 5):
    return {"inventory_status": 1}

@router.put("/{product_id}", tags=['inventory'])
async def inventory_update(product_id):
    return {"product_id": product_id, "amount": 10}

@router.delete("/clear", tags=['inventory'])
async def inventory_clear():
    return {"status": "cleared"}