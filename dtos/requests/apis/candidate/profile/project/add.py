from pydantic import BaseModel
from typing import Optional


class AddCandidateProjectRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    title: str
    description: str
    project_url: Optional[str]