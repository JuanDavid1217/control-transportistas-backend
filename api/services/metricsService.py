from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import MetricaBase, NuevaMetrica, Metrica
from repository import metricsRepository
from services import routeService
from utils.validatorUtils import esNumeroValido
from handlerException.handlerExceptionManager import handleValidationError

def crear(db: Session, nuevaMetrica: NuevaMetrica):
    handleValidationError(esNumeroValido(nuevaMetrica.distancia, "distancia"))
    handleValidationError(esNumeroValido(nuevaMetrica.combustible, "combustible"))
    ruta = routeService.obtener(db, nuevaMetrica.id)
    existe = metricsRepository.obtener(db, nuevaMetrica.id)
    if existe is None:
        routeService.validarRutaCompletada(ruta)
        metrica = metricsRepository.crear(db, nuevaMetrica)
        return Metrica.from_orm(metrica)
    raise HTTPException(status_code=409, detail=f"Metrica ya registrada.")

def obtener(db: Session, id:int):
    metrica = metricsRepository.obtener(db, id)
    if metrica is None:
        raise HTTPException(status_code=404, detail="Metrica no encontrada.")
    return Metrica.from_orm(metrica)

def obtenerTodos(db: Session):
    return [Metrica.from_orm(metrica) for metrica in metricsRepository.obtenerTodos(db)]

def actualizar(db: Session, id:int, nuevaMetrica: MetricaBase):
    handleValidationError(esNumeroValido(nuevaMetrica.distancia, "distancia"))
    handleValidationError(esNumeroValido(nuevaMetrica.combustible, "combustible"))
    metrica = obtener(db, id)
    metrica = metricsRepository.actualizar(db, id, nuevaMetrica)
    return Metrica.from_orm(metrica)

def eliminar(db: Session, id:int):
    eliminado = metricsRepository.eliminar(db, id)
    if eliminado is None:
        raise HTTPException(status_code=404, detail="Metrica no encontrada.")
    return True