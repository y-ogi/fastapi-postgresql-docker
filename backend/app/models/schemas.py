from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BaseModelSchema(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class ItemSchema(BaseModelSchema):
    name: str

    

