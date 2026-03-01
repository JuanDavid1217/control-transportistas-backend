from fastapi import HTTPException


def handleGlobalException(exc: Exception):
    if isinstance(exc, HTTPException):
        raise exc
    raise HTTPException(status_code=409, detail=str(exc))

def handleValidationError(message):
    if message:
        raise HTTPException(status_code=409, detail=message)