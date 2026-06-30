from fastapi import APIRouter
from app.schemas.customer import CustomerCreate

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

customers = []


@router.post("")
def create_customer(customer: CustomerCreate):
    customers.append(customer)

    return {
        "message": "Customer created",
        "customer": customer
    }


@router.get("")
def get_customers():
    return customers