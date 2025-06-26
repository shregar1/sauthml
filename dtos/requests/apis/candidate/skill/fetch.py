from pydantic import BaseModel
from typing import Optional


class FetchCandidateSkillsRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    some_optional_param: Optional[int] = None