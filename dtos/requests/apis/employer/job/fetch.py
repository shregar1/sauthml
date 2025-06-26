from pydantic import BaseModel


class FetchEmployerJobsRequestDTO(BaseModel):

    reference_number: str
    user_urn: str