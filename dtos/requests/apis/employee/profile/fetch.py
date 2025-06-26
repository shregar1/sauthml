from pydantic import BaseModel


class FetchEmployeeProfileRequestDTO(BaseModel):

    reference_number: str
    user_urn: str