from pydantic import BaseModel


class DeleteCandidateWorkExperienceRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    work_experience_urn: str