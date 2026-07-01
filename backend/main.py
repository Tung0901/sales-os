from fastapi import FastAPI

from app.database.database import Base, engine
import app.models

from app.routers.customer import router as customer_router
from app.routers.product import router as product_router
from app.routers.project import router as project_router
# Tạo database và các bảng nếu chưa tồn tại
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SalesOS API",
    version="0.1.0",
    description="Sales Operating System"
)

app.include_router(customer_router)
app.include_router(product_router)
app.include_router(project_router)
app.include_router(product_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to SalesOS"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "database": "connected"
    }


@app.get("/version")
def version():
    return {
        "version": "0.1.0"
    }