from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import MetricaBase, NuevaMetrica
from repository import metricsRepository
from services import routeService

def crear(db: Session, nuevaMetrica: NuevaMetrica):
    ruta = routeService.obtener(db, nuevaMetrica.id)
    existe = metricsRepository.obtener(db, nuevaMetrica.id)
    if existe is None:
        routeService.validarRutaCompletada(ruta)
        metrica = metricsRepository.crear(db, nuevaMetrica)
        return metrica
    raise HTTPException(status_code=409, detail=f"Metrica ya registrada.")

def obtener(db: Session, id:int):
    metrica = metricsRepository.obtener(db, id)
    if metrica is None:
        raise HTTPException(status_code=404, detail="Metrica no encontrada.")
    return metrica

def obtenerTodos(db: Session):
    return metricsRepository.obtenerTodos(db)

def actualizar(db: Session, id:int, nuevaMetrica: MetricaBase):
    metrica = obtener(db, id)
    metrica = metricsRepository.actualizar(db, id, nuevaMetrica)
    return metrica

def eliminar(db: Session, id:int):
    eliminado = metricsRepository.eliminar(db, id)
    if eliminado is None:
        raise HTTPException(status_code=404, detail="Metrica no encontrada.")
    return True