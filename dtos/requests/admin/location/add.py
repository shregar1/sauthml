from pydantic import BaseModel


class AddLocationRequestDTO(BaseModel):

    reference_number: str
    city: str
    state: str
    country: str
    country_code: str
    pin_code: str 