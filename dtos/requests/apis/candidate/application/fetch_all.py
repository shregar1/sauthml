from pydantic import BaseModel


class CandidateFetchJobApplicationsRequestDTO(BaseModel):

    reference_number: str