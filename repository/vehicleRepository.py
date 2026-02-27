from sqlalchemy.orm import Session
from models.models import Unidad
from schemas.schemas import NuevaUnidad

def crear(db: Session, nuevaUnidad: NuevaUnidad):
    try:
        unidad = Unidad(placa=nuevaUnidad.placa, marca=nuevaUnidad.marca, modelo=nuevaUnidad.modelo, anio=nuevaUnidad.anio, usuarioId=nuevaUnidad.usuarioId)
        db.add(unidad)
        db.commit()
        db.refresh(unidad)
        return unidad
    except Exception as e:
        db.rollback()
        raise e

def obtener(db: Session, id: int):
    unidad = db.query(Unidad).filter(Unidad.id == id).first()
    return unidad

def obtenerTodos(db: Session):
    unidades = db.query(Unidad).all()
    return unidades

def obtenerPorPlaca(db: Session, placa: str):
    unidad = db.query(Unidad).filter(Unidad.placa == placa).first()
    return unidad

def actualizar(db: Session, id:int, nuevaUnidad: NuevaUnidad):
    unidad = obtener(db, id)
    if unidad:
        try:
            unidad.placa = nuevaUnidad.placa
            unidad.marca = nuevaUnidad.marca
            unidad.modelo = nuevaUnidad.modelo
            unidad.anio = nuevaUnidad.anio
            unidad.usuarioId = nuevaUnidad.usuarioId
            db.commit()
            db.refresh(unidad)
            return unidad
        except Exception as e:
            db.rollback()
            raise e
    return None

def eliminar(db: Session, id: int):
    unidad = obtener(db, id)
    if unidad:
        try:
            db.delete(unidad)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            raise e
    return None
