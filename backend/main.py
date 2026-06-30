from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.customer import Customer
from app.routers.customer import router as customer_router

# Tạo database và các bảng nếu chưa tồn tại
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SalesOS API",
    version="0.1.0",
    description="Sales Operating System"
)

app.include_router(customer_router)


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