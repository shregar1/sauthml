from pydantic import BaseModel
from typing import Optional


class FetchJobRequestDTO(BaseModel):

    reference_number: str
    skills: Optional[list]
    location: Optional[list]
    min_year_of_experience: Optional[int]