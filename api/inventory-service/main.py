from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import product_route, inventory_route
import os


app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

product_enabled = os.getenv('PRODUCT_ENABLED', 'y')
inventory_enabled = os.getenv('INVENTORY_ENABLED', 'y')

# app.include_router(product.router, prefix='/api/v1/product/')
if product_enabled == 'y':
    app.include_router(product_route.router, prefix='/api/v1/product')
if inventory_enabled == 'y':
    app.include_router(inventory_route.router, prefix='/api/v1/inventory')