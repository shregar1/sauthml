from pydantic import BaseModel


class CandidateFetchJobApplicationRequestDTO(BaseModel):

    reference_number: str
    job_urn: str
    offset: int
    limit: int