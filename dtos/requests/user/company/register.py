from pydantic import BaseModel


class RegisterCompanyRequestDTO(BaseModel):

    reference_number: str
    token: str
    password: str
    website: str
    description: str
    country_code: str
    contact_number: str
    established_in: int
