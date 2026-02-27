from sqlalchemy.orm import Session
from models.models import Estatus

def obtener(db: Session, id: int):
    estatus = db.query(Estatus).filter(Estatus.id == id).first()
    return estatus

def obtenerTodos(db: Session):
    estatus = db.query(Estatus).all()
    return estatus
