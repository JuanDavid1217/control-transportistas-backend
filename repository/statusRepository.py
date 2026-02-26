from sqlalchemy.orm import Session
from models import models

def obtener(db: Session, id: int):
    estatus = db.query(models.Estatus).filter(models.Estatus.id == id).first()
    return estatus

def obtenerTodos(db: Session):
    estatus = db.query(models.Estatus).all()
    return estatus
