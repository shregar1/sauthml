from pydantic import BaseModel


class DeleteCandidateProjectRequestDTO(BaseModel):

    reference_number: str
    user_urn: str
    project_urn: str