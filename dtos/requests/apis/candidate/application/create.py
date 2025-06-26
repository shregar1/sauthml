from pydantic import BaseModel


class CreateJobApplicationRequestDTO(BaseModel):

    reference_number: str
    job_urn: str