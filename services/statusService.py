from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import Estatus
from repository import statusRepository

def obtener(db: Session, id:int):
    estatus = statusRepository.obtener(db, id)
    if estatus is None:
        raise HTTPException(status_code=404, detail="Estatus no enontrado.")
    return estatus

def obtenerTodos(db: Session):
    return statusRepository.obtenerTodos(db)