from pydantic import BaseModel


class ScheduleInterviewRequestDTO(BaseModel):

    reference_number: str
    job_urn: str
    company_urn: str
    candidate_urn: str
    status: str
    start_at: str
    end_at: str
    url: str