from fastapi import FastAPI

from app.database import Base, engine
from app.routers import products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Catalog API",
    description="Learning Redis with FastAPI + PostgreSQL",
)

app.include_router(products.router)


@app.get("/health")
def health():
    return {"status": "ok"}