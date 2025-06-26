from pydantic import BaseModel


class DeleteCandidateSkillRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    skill_urn: str