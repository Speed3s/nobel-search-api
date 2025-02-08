from pydantic import BaseModel, Field
from typing import List, Optional

class Laureate(BaseModel):
    id: str
    firstname: str
    surname: Optional[str] = None
    motivation: str

class Prize(BaseModel):
    year: str
    category: str
    laureates: List[Laureate]
