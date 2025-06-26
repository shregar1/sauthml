from pydantic import BaseModel


class InterviewerFetchProfileRequestDTO(BaseModel):

    reference_number: str
    user_urn: str