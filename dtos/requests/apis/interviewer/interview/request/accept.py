from pydantic import BaseModel


class InterviewerAcceptInterviewRequestDTO(BaseModel):

    reference_number: str
    interview_request_urn: str