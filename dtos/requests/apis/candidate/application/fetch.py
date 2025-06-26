from pydantic import BaseModel


class CandidateFetchJobApplicationRequestDTO(BaseModel):

    reference_number: str
    application_urn: str