from pydantic import BaseModel
from typing import Optional


class FetchCandidateProfilesRequestDTO(BaseModel):

    reference_number: str
    skills: Optional[list] = []
    min_year_of_experience: Optional[int] = 0