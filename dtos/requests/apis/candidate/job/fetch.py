from pydantic import BaseModel


class FetchCandidateJobRequestDTO(BaseModel):

    reference_number: str
    job_urn: str