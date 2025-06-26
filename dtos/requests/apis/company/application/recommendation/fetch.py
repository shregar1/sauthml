from pydantic import BaseModel


class CompanyFetchRecommendedApplicationsRequestDTO(BaseModel):

    reference_number: str