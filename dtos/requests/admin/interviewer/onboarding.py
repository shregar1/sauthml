from pydantic import BaseModel


class AdminInterviewerOnboardingEmailRequestDTO(BaseModel):

    reference_number: str
    email: str