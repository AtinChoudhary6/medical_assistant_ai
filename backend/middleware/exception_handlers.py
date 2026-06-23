from fastapi import Request
from fastapi.responses import JSONResponse
from logger import logger


async def global_exception_handler(request: Request, exc: Exception):
    """
    Catches any exception that isn't handled inside a route and
    returns a clean JSON error instead of a raw stack trace.
    """
    logger.error(f"Unhandled error on {request.url.path}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again."},
    )
