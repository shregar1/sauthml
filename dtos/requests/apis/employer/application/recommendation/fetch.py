from pydantic import BaseModel


class EmployerFetchRecommendedApplicationsRequestDTO(BaseModel):

    reference_number: str