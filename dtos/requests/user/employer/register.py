from pydantic import BaseModel
from typing import Optional


class RegisterEmployerRequestDTO(BaseModel):

    reference_number: str
    token: str
    password: str
    first_name: str
    last_name: Optional[str] = None
    summary: str = None
    country_code: str
    phone_number: str
    whatsapp_number: Optional[str]
