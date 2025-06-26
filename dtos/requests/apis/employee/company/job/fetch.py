from pydantic import BaseModel


class EmployeeFetchCompanyJobsRequestDTO(BaseModel):

    reference_number: str
    company_urn: str