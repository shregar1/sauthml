from pydantic import BaseModel


class CreateEmployerProfileRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    company_urn: str
    first_name: str
    last_name: str
    summary: str
    country_code: str
    phone_number: str
    whatsapp_number: str