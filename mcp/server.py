# mcp_server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import requests
from datetime import date
from uuid import UUID
from fastapi.middleware.cors import CORSMiddleware

MCP_BACKEND_URL = "http://localhost:8000"  # Replace with your actual backend URL

app = FastAPI()

# Enable CORS for all origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    id: UUID
    serial_number: str
    manufacturing_date: date

class ProductCreate(BaseModel):
    serial_number: str
    manufacturing_date: date

class ProductUpdate(BaseModel):
    serial_number: Optional[str] = None
    manufacturing_date: Optional[date] = None

@app.get("/products", response_model=List[Product])
def list_products():
    response = requests.get(f"{MCP_BACKEND_URL}/products/")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.post("/products", response_model=Product)
def add_product(product: ProductCreate):
    response = requests.post(f"{MCP_BACKEND_URL}/products/", json=product.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: UUID):
    response = requests.delete(f"{MCP_BACKEND_URL}/products/{product_id}")
    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.patch("/products/{product_id}", response_model=Product)
def update_product(product_id: UUID, update: ProductUpdate):
    response = requests.patch(f"{MCP_BACKEND_URL}/products/{product_id}", json=update.dict(exclude_unset=True))
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()
