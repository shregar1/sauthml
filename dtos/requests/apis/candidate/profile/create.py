from pydantic import BaseModel
from typing import Optional


class CreateCandidateProfileRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    first_name: str
    last_name: str
    summary: str
    total_experience_months: int
    country_code: str
    phone_number: str
    whatsapp_country_code: str
    whatsapp_number: str
    location_urn: str
    currency: str
    current_ctc: int
    expected_ctc: int
    hourly_rate: int
    notice_period_days: int
    website_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    social_links: Optional[dict] = {}