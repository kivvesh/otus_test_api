from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class Brewery(BaseModel):
    id: str = Field(..., description="Unique identifier for the brewery")
    name: str = Field(..., description="Name of the brewery")
    brewery_type: str = Field(..., description="Type of the brewery (e.g., micro, regional)")
    address_1: str = Field(..., description="Primary address of the brewery")
    address_2: Optional[str] = Field(None, description="Secondary address of the brewery (if any)")
    address_3: Optional[str] = Field(None, description="Tertiary address of the brewery (if any)")
    city: str = Field(..., description="City where the brewery is located")
    state_province: str = Field(..., description="State or province where the brewery is located")
    postal_code: str = Field(..., description="Postal code of the brewery's location")
    country: str = Field(..., description="Country where the brewery is located")
    longitude: str = Field(..., description="Longitude coordinate of the brewery")
    latitude: str = Field(..., description="Latitude coordinate of the brewery")
    phone: str = Field(..., description="Contact phone number for the brewery")
    website_url: HttpUrl = Field(..., description="Website URL of the brewery")
    state: str = Field(..., description="State where the brewery is located")
    street: str = Field(..., description="Street address of the brewery")

