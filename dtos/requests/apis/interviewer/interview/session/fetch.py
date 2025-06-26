from pydantic import BaseModel


class InterviewerFetchInterviewsDTO(BaseModel):

    reference_number: str