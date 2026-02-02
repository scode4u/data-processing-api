import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ","_")
    )
    df = df.drop_duplicates()

    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())
    
    for col in df.select_dtypes(include="object").columns:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
    
    for col in df.columns:
        converted = pd.to_numeric(df[col], errors="coerce")

    if converted.notna().sum() > 0:
        df[col] = converted.fillna(0)

    return df

