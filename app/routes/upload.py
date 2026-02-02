from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

from app.services.cleaner import clean_dataframe
from app.schemas.responses import upload_responsive_model

router = APIRouter()

DATA_STORE = {}

@router.post("/", response_model=upload_responsive_model)
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid File type. Only CSV's are allowed.")

    try:
        df = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(
            status_code=422,
            detail="Failed to read CSV."
        )
    
    if df.empty:
        raise HTTPException(
            status_code=422,
            detail="Uploaded CSV file is empty."
        )
    
    cleaned_df = clean_dataframe(df)

    
    DATA_STORE["raw"] = df
    DATA_STORE["cleaned"] = cleaned_df


    return {
        "status": "success",
        "rows": df.shape[0],
        "columns": list(df.columns)
    }
