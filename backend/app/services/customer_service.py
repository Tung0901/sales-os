from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate


def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(
        customer_code=f"CUS{customer.phone[-4:]}",
        name=customer.name,
        phone=customer.phone,
        email=customer.email,
        address=customer.address,
        customer_type=customer.customer_type,
        source=customer.source,
        status="Lead",
        note=customer.note,
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


def get_customers(db: Session):
    return db.query(Customer).all()