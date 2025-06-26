from pydantic import BaseModel
from typing import List


class AddCandidateSkillRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    skills: List[str]