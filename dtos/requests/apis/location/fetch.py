from pydantic import BaseModel


class FetchLocationsRequestDTO(BaseModel):

    reference_number: str