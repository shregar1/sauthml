from pydantic import BaseModel


class AdminCompanyOnboardingEmailRequestDTO(BaseModel):

    reference_number: str
    email: str
    name: str