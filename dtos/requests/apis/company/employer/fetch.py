from pydantic import BaseModel


class FetchCompanyEmployersRequestDTO(BaseModel):

    reference_number: str