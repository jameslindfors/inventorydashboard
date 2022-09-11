from fastapi import FastAPI

app = FastAPI()


@app.get("/inventory")
async def root():
    return {"message": "Inventory-Service"}