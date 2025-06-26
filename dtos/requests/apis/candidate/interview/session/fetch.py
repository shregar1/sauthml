from pydantic import BaseModel


class CandidateFetchInterviewRequestDTO(BaseModel):

    reference_number: str