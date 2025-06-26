from pydantic import BaseModel


class CandidateCreateInterviewRequestRequestDTO(BaseModel):

    reference_number: str
    application_urn: str
    start_at: str