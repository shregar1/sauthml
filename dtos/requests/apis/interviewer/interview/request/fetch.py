from pydantic import BaseModel


class InterviewerFetchInterviewRequestsDTO(BaseModel):

    reference_number: str