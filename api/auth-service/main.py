from fastapi import FastAPI, Request, Response, status

app = FastAPI()

@app.get("/authenticated")
async def root(request: Request, response: Response):
    authString = request.headers.get("authorization")
    if authString == "asdfghjkl;":
        response.status_code = status.HTTP_200_OK
        return {"Authenticated": True}
    
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"Authorized": False}