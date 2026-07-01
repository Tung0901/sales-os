from pydantic import BaseModel


class ProjectCreate(BaseModel):
    customer_id: int
    name: str
    address: str | None = None
    note: str | None = None