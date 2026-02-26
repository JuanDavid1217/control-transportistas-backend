from sqlalchemy.orm import Session, func
from models import models
from schemas import schemas

def crear(db: Session, nuevaRuta: schemas.NuevaRuta):
    try:
        ruta = models.Ruta(unidadId=nuevaRuta.unidadId, inicio=nuevaRuta.inicio, destino=nuevaRuta.destino)
        db.add(ruta)
        db.commit()
        db.refresh(ruta)
        return ruta
    except Exception as e:
        db.rollback()
        raise e

def obtener(db: Session, id: int):
    ruta = db.query(models.Ruta).filter(models.Ruta.id == id).first()
    return ruta

def obtenerTodos(db: Session):
    rutas= db.query(models.Ruta).all()
    return rutas

def actualizar(db: Session, id:int, nuevaRuta: schemas.NuevaRuta):
    ruta = obtener(db, id)
    if ruta:
        try:
            ruta.unidadId = nuevaRuta.unidadId
            ruta.inicio = nuevaRuta.inicio
            ruta.destino = nuevaRuta.destino
            db.commit()
            db.refresh(ruta)
            return ruta
        except Exception as e:
            db.rollback()
            raise e
    return None

def eliminar(db: Session, id: int):
    ruta = obtener(db, id)
    if ruta:
        try:
            db.delete(ruta)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            raise e
    return None

def iniciar(db:Session, id:int):
    ruta = obtener(db, int)
    if ruta:
        try:
            ruta.estatus = 2
            ruta.horaInicio = func.now()
            db.commit()
            db.refresh(ruta)
            return ruta
        except Exception as e:
            db.rollback()
            raise e
    return None

def completar(db:Session, id:int):
    ruta = obtener(db, int)
    if ruta:
        try:
            ruta.estatus = 3
            ruta.horaFin = func.now()
            db.commit()
            db.refresh(ruta)
            return ruta
        except Exception as e:
            db.rollback()
            raise e
    return None