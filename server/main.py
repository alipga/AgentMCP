# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from uuid import UUID, uuid4

app = FastAPI()

# In-memory storage for simplicity
products_db = {}

# Pydantic model
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

@app.post("/products/", response_model=Product)
def add_product(product: ProductCreate):
    new_product = Product(id=uuid4(), **product.dict())
    products_db[str(new_product.id)] = new_product
    return new_product

@app.get("/products/", response_model=List[Product])
def list_products():
    return list(products_db.values())

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: UUID):
    pid = str(product_id)
    if pid in products_db:
        del products_db[pid]
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@app.patch("/products/{product_id}", response_model=Product)
def update_product(product_id: UUID, update: ProductUpdate):
    pid = str(product_id)
    if pid not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    existing = products_db[pid]
    updated = existing.copy(update=update.dict(exclude_unset=True))
    products_db[pid] = updated
    return updated
