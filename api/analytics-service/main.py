from fastapi import FastAPI

app = FastAPI()


@app.get("/analytics")
async def root():
    return {"message": "Analytics-Service"}