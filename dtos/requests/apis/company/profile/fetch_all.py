from pydantic import BaseModel


class FetchCompanyProfilesRequestDTO(BaseModel):

    reference_number: str