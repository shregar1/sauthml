from pydantic import BaseModel
from typing import Optional


class CreateJobRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    designation: str
    description: str
    role_and_responsibilities: Optional[str]
    work_expectations: Optional[str]
    cultural_expectations: Optional[str]
    currency: str
    start_salary_amount: float
    end_salary_amount: float
    min_years_of_experience: int
    max_years_of_experience: int
    skills: list
    is_prescreening_interview_required: bool
    interview_difficulty: str
    interview_duration: str
    locations: list
    is_fulltime: bool