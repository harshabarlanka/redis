from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str
    description: str = ""
    price: Decimal = Field(gt=0)
    stock: int = Field(ge=0)


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    stock: int | None = None


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    stock: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True