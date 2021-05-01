from typing import Optional

from pydantic.main import BaseModel


class Location(BaseModel):
    city: str = 'Puchong'
    state: Optional[str] = None
    country: Optional[str] = 'my'
