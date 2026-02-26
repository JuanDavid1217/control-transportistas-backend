from fastapi import HTTPException


def global_exception_handler(exc: Exception):
    if isinstance(exc, HTTPException):
        raise exc
    raise HTTPException(status_code=500, detail=str(exc))