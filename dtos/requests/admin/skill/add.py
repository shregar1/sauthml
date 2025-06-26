from pydantic import BaseModel


class AddSkillRequestDTO(BaseModel):

    reference_number: str
    code: str
    description: str
    value: str