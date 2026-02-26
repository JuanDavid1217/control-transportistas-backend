from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def crear(db: Session, rutaId:int, nuevaMetrica: schemas.NuevaMetrica):
    try:
        metrica = models.MetricaPorRuta(id=rutaId, distancia=nuevaMetrica.distancia, combustible=nuevaMetrica.combustible)
        db.add(metrica)
        db.commit()
        db.refresh(metrica)
        return metrica
    except Exception as e:
        db.rollback()
        raise e

def obtener(db: Session, id: int):
    metrica = db.query(models.MetricaPorRuta).filter(models.MetricaPorRuta.id == id).first()
    return metrica

def obtenerTodos(db: Session):
    metricas = db.query(models.Metricas).all()
    return metricas

def actualizar(db: Session, id:int, nuevaMetrica: schemas.NuevaMetrica):
    metrica = obtener(db, id)
    if metrica:
        try:
            metrica.distancia = nuevaMetrica.distancia
            metrica.combustible = nuevaMetrica.combustible
            db.commit()
            db.refresh(metrica)
            return metrica
        except Exception as e:
            db.rollback()
            raise e
    return None

def eliminar(db: Session, id: int):
    metrica = obtener(db, id)
    if metrica:
        try:
            db.delete(metrica)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            raise e
    return None
