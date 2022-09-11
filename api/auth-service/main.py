from fastapi import FastAPI

app = FastAPI()


@app.get("/auth")
async def root():
    return {"message": "Auth-Service"}

@app.get("/authenticated")
async def root():
    return {"message": "Authenticated"}