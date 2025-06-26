from pydantic import BaseModel
from typing import Optional, List


class FetchCandidateJobsRequestDTO(BaseModel):

    reference_number: str
    skills: Optional[List[str]] = []
    min_year_of_experience: Optional[int]
    locations: Optional[List[str]] = []
    page: int