from pydantic import BaseModel


class DeleteJobRequestDTO(BaseModel):

    reference_number: str
    job_urn: str