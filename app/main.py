from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.routes import analytics, upload
from app.schemas.responses import error_responsive_model
from fastapi.exceptions import RequestValidationError

app = FastAPI(title="Data Processing API",
              version='1.0.0')


app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])

@app.get('/')
def root():
    return {    
        "Status": "Running"
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=error_responsive_model(
            error="HTTPException",
            message=str(exc.detail),
            status_code=exc.status_code
        ).model_dump()
    )

@app.exception_handler(ValueError)
async def value_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=422,
        content=error_responsive_model(
            error="ValueException",
            message="Invalid Request Validator",
            status_code=422
        ).model_dump()
    )

@app.exception_handler(Exception)
async def exceptional_error(request: Request, exc: Exception):
    JSONResponse(
        status_code=500,
        content=error_responsive_model(
            error="Internal Server Error",
            message="An Unexpected error found",
            status_code=500

        ).model_dump()
    )
