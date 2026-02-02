from pydantic import BaseModel
from typing import Any, List, Dict

class aggregate_response_model(BaseModel):

    column: str
    operation: str
    value: float


class summary_responsive_model(BaseModel):
    row: int
    columns: int
    number_summary: dict[str, dict[str, float]]


class upload_responsive_model(BaseModel):

    status: str
    rows: int
    columns: list[str]

class top_responsive_model(BaseModel):
    column: str
    top: int
    data: list[dict[str,Any]]


class filter_responsive_model(BaseModel):
    rows: int
    column: List[dict[str,Any]]

class error_responsive_model(BaseModel):
    error: str
    message: str
    status_code: int