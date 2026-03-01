from sqlalchemy import text
from sqlalchemy.orm import Session
from models.models import MetricaPorRuta
from schemas.schemas import MetricaBase, NuevaMetrica

def crear(db: Session, nuevaMetrica: NuevaMetrica):
    try:
        metrica = db.execute(text('SELECT * FROM "guardarMetrica"(:id, :distancia, :combustible)'),
                            {
                                "id": nuevaMetrica.id,
                                "distancia": nuevaMetrica.distancia,
                                "combustible": nuevaMetrica.combustible
                            })
        db.commit()
        return metrica.fetchone()
    except Exception as e:
        db.rollback()
        raise e

def obtener(db: Session, id: int):
    metrica = db.query(MetricaPorRuta).filter(MetricaPorRuta.id == id).first()
    return metrica

def obtenerTodos(db: Session):
    metricas = db.query(MetricaPorRuta).all()
    return metricas

def actualizar(db: Session, id:int, nuevaMetrica: MetricaBase):
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
