from pydantic import BaseModel


class FetchCurrenciesRequestDTO(BaseModel):

    reference_number: str