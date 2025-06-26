from pydantic import BaseModel
from typing import Optional


class AddCandidateEducationQualificationRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    from_date: str
    is_current: bool
    to_date: Optional[str]
    location_urn: str
    organisation: str
    description: str
    organisation_url: Optional[str]