from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    if "json" in str(exc):
        print(str(exc))
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": "You provided an invalid JSON format", 
                "errors": exc.errors()
                },
        )
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()},
    )

async def validation_response_exception_handler(response: Response, exc: ResponseValidationError):
    """
    print(exc)
    if "validation errors" in str(exc):
        error_fields = [str(e['loc'][-1]) for e in exc.errors()]
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": f"Requested object doesn't fulfill minimum requirements for the fields: {", ".join(error_fields)} ", 
                "errors": exc.errors()
                },
        )
        """
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()},
    )