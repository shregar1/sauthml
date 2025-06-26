from pydantic import BaseModel


class DeleteCandidateEducationQualificationRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    education_qualification_urn: str