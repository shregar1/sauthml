from pydantic import BaseModel


class FetchCompanyJobsRequestDTO(BaseModel):

    reference_number: str