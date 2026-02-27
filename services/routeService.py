from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import NuevaRuta
from repository import routeRepository
from services import vehicleService

def crear(db: Session, nuevaRuta: NuevaRuta):
    vehicleService.obtener(db, nuevaRuta.unidadId)
    ruta = routeRepository.crear(db, nuevaRuta)
    return ruta

def obtener(db: Session, id:int):
    ruta = routeRepository.obtener(db, id)
    if ruta is None:
        raise HTTPException(status_code=404, detail="Ruta no encontrada.")
    return ruta

def obtenerTodos(db: Session):
    return routeRepository.obtenerTodos(db)

def actualizar(db: Session, id:int, nuevaRuta: NuevaRuta):
    ruta = obtener(db, id)
    vehicleService.obtener(db, nuevaRuta.unidadId)
    validarRutaNoIniciada(ruta)
    ruta = routeRepository.actualizar(db, id, nuevaRuta)
    return ruta 

def eliminar(db: Session, id:int):
    ruta = obtener(db, id)
    validarRutaNoIniciada(ruta)
    routeRepository.eliminar(db, id)

def iniciar(db:Session, id:int):
    ruta = obtener(db, id)
    validarRutaNoIniciada(ruta)
    validarRutaNoCompletada(ruta)
    return routeRepository.iniciar(db, id)

def completar(db:Session, id:int):
    ruta = obtener(db, id)
    validarRutaIniciada(ruta)
    validarRutaNoCompletada(ruta)
    return routeRepository.completar(db, id)

def validarRutaIniciada(ruta):
    if ruta.estatusId == 1:
        raise HTTPException(status_code=409, detail="La ruta no ha sido iniciada")

def validarRutaNoIniciada(ruta):
    if ruta.estatusId == 2:
        raise HTTPException(status_code=409, detail="La ruta ya ha sido iniciada.")

def validarRutaNoCompletada(ruta):
    if ruta.estatusId == 3:
        raise HTTPException(status_code=409, detail="La ruta ya ha sido completada.")

def validarRutaCompletada(ruta):
    if ruta.estatusId != 3:
        raise HTTPException(status_code=409, detail="La ruta no ha sido completada.")