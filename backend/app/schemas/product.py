from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    code: str
    unit: str
    price: int


class ProductResponse(BaseModel):
    id: int
    name: str
    code: str
    unit: str
    price: int

    model_config = {
        "from_attributes": True
    }