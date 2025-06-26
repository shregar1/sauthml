from pydantic import BaseModel


class FetchCompanyRequestDTO(BaseModel):

    reference_number: str
    user_urn: str