from pydantic import BaseModel


class FetchSkillsRequestDTO(BaseModel):

    reference_number: str