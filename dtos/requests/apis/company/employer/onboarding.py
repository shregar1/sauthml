from pydantic import BaseModel


class CompanyEmployerOnbardingEmailRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    email: str