from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import product_route, inventory_route
from db import database
import os

app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

database.init_db(app)

product_enabled = os.getenv('PRODUCT_ENABLED', 'y')
inventory_enabled = os.getenv('INVENTORY_ENABLED', 'y') 

if product_enabled == 'y':
    app.include_router(product_route.router, prefix='/inventory/api/p')
if inventory_enabled == 'y':
    app.include_router(inventory_route.router, prefix='/inventory/api/i')