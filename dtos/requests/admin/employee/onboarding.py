from pydantic import BaseModel


class AdminEmployeeOnboardingEmailRequestDTO(BaseModel):

    reference_number: str
    email: str