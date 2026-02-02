from fastapi import APIRouter, Query, HTTPException
import pandas as pd

from app.routes.upload import DATA_STORE
from app.services.utils import to_python
from app.schemas.responses import aggregate_response_model, summary_responsive_model, filter_responsive_model, top_responsive_model

router = APIRouter()

def get_df() -> pd.DataFrame:
    if "raw" not in DATA_STORE:
        raise HTTPException(
            status_code=400,
            detail="No CSV uploaded yet."
        )
    
    if "cleaned" not in DATA_STORE:
        raise HTTPException(
            status_code=404,
            detail="No cleaned Data available. Upload a CSV first"
        )
    
    return DATA_STORE["cleaned"]

@router.get("/summary", response_model=summary_responsive_model)
def summary():
    df = get_df()

    number_summary = df.describe(include="number").astype(float).to_dict()

    return{
        "row": df.shape[0],
        "columns": df.shape[1],
        "number_summary": number_summary
    }

@router.get("/aggregate",response_model=aggregate_response_model)
def aggregate(
    column: str = Query(...),
    operation: str = Query(..., pattern="^(sum|avg|min|max|count)$")):

    df = get_df()

    if column not in df.columns:
        raise HTTPException(
            status_code= 400,
            detail=f"Column '{column}' not found"
        )
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise HTTPException(
            status_code=400,
            detail=f"columns '{column}' must be numeric"
        )
    
    operations = {
        "sum" : df[column].sum(),
        "avg" : df[column].mean(),
        "min" : df[column].min(),
        "max" : df[column].max(),
        "count" : df[column].count()
    }

    return {
        "column": column,
        "operation": operation,
        "value": to_python(operations[operation])
    }

@router.get("/filter",response_model=filter_responsive_model)
def filter_data(
    column : str = Query(...),
    value : int = Query(...)
):
    df = get_df()

    if column not in df.columns:
        raise HTTPException(
            status_code=400,
            detail=f"Columns {column} not found."
        )
    
    filter_df = df[df[column].astype(str) == value]

    return{
        "rows": filter_df.shape[0],
        "column": filter_df.head(10).to_dict(orient="records")
    }

@router.get("/top", response_model=top_responsive_model)
def top(
    column: str = Query(...),
    n: int = Query(5, gt=0)
):
    df = get_df()

    if column not in df.columns:
        raise HTTPException(
            status_code= 400,
            detail=f"column '{column}' not found"
        )
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise HTTPException(
            status_code=404,
            detail=f"Column {column} must be numeric"
        )
    
    top_df = df.sort_values(by=column, ascending=False).head(n)

    return{
        "column": column,
        "top": n,
        "data": top_df.to_dict(orient="records")
    }
