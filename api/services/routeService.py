from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import NuevaRuta, Ruta
from repository import routeRepository
from services import vehicleService
from utils.validatorUtils import estaVacio
from handlerException.handlerExceptionManager import handleValidationError

def crear(db: Session, nuevaRuta: NuevaRuta):
    handleValidationError(estaVacio(nuevaRuta.inicio, "inicio"))
    handleValidationError(estaVacio(nuevaRuta.destino, "destino"))
    vehicleService.obtener(db, nuevaRuta.unidadId)
    ruta = routeRepository.crear(db, nuevaRuta)
    return Ruta.from_orm(ruta)

def obtener(db: Session, id:int):
    ruta = routeRepository.obtener(db, id)
    if ruta is None:
        raise HTTPException(status_code=404, detail="Ruta no encontrada.")
    return Ruta.from_orm(ruta)

def obtenerTodos(db: Session):
    rutas = routeRepository.obtenerTodos(db)
    return [Ruta.from_orm(ruta) for ruta in rutas]

def actualizar(db: Session, id:int, nuevaRuta: NuevaRuta):
    handleValidationError(estaVacio(nuevaRuta.inicio, "inicio"))
    handleValidationError(estaVacio(nuevaRuta.destino, "destino"))
    ruta = obtener(db, id)
    vehicleService.obtener(db, nuevaRuta.unidadId)
    validarRutaNoIniciada(ruta)
    ruta = routeRepository.actualizar(db, id, nuevaRuta)
    return Ruta.from_orm(ruta) 

def eliminar(db: Session, id:int):
    ruta = obtener(db, id)
    validarRutaNoIniciada(ruta)
    routeRepository.eliminar(db, id)

def iniciar(db:Session, id:int):
    ruta = obtener(db, id)
    validarRutaNoIniciada(ruta)
    validarRutaNoCompletada(ruta)
    return Ruta.from_orm(routeRepository.iniciar(db, id))

def completar(db:Session, id:int):
    ruta = obtener(db, id)
    validarRutaIniciada(ruta)
    validarRutaNoCompletada(ruta)
    return Ruta.from_orm(routeRepository.completar(db, id))

def validarRutaIniciada(ruta):
    if ruta.estatus.id == 1:
        raise HTTPException(status_code=409, detail="La ruta no ha sido iniciada")

def validarRutaNoIniciada(ruta):
    if ruta.estatus.id == 2:
        raise HTTPException(status_code=409, detail="La ruta ya ha sido iniciada.")

def validarRutaNoCompletada(ruta):
    if ruta.estatus.id == 3:
        raise HTTPException(status_code=409, detail="La ruta ya ha sido completada.")

def validarRutaCompletada(ruta):
    if ruta.estatus.id != 3:
        raise HTTPException(status_code=409, detail="La ruta no ha sido completada.")