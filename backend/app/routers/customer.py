from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.services import customer_service

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("", response_model=CustomerResponse)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return customer_service.create_customer(db, customer)


@router.get("", response_model=list[CustomerResponse])
def get_customers(
    db: Session = Depends(get_db)
):
    return customer_service.get_customers(db)