from pydantic import BaseModel
from typing import List


class Location(BaseModel):
    type: str
    coordinates: List[float]
    is_location_exact: bool


class Address(BaseModel):
    street: str
    government_area: str
    market: str
    country: str
    country_code: str
    location: Location
