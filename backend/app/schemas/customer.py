from pydantic import BaseModel
from datetime import datetime


class CustomerCreate(BaseModel):
    name: str
    phone: str
    email: str | None = None
    address: str | None = None
    customer_type: str
    source: str
    note: str | None = None


class CustomerResponse(BaseModel):
    id: int
    customer_code: str | None
    name: str
    phone: str
    email: str | None
    address: str | None
    customer_type: str | None
    source: str | None
    status: str | None
    note: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }