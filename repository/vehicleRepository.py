from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def crear(db: Session, nuevaUnidad: schemas.NuevaUnidad):
    try:
        unidad = models.Unidad(placa=nuevaUnidad.placa, marca=nuevaUnidad.marca, modelo=nuevaUnidad.modelo, anio=nuevaUnidad.anio, usuarioId=nuevaUnidad.UsuarioId)
        db.add(unidad)
        db.commit()
        db.refresh(unidad)
        return unidad
    except Exception as e:
        db.rollback()
        raise e

def obtener(db: Session, id: int):
    unidad = db.query(models.Unidad).filter(models.Unidad.id == id).first()
    return unidad

def obtenerTodos(db: Session):
    unidades = db.query(models.Unidades).all()
    return unidades

def actualizar(db: Session, id:int, nuevaUnidad: schemas.NuevaUnidad):
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
