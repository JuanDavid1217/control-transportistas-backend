from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import NuevaUnidad
from repository import vehicleRepository
from services import userService
from services.validatorService import estaVacio, formatoPlaca, anioValido
from handlerException.handlerExceptionManager import handleValidationError

def crear(db: Session, nuevaUnidad: NuevaUnidad):
    handleValidationError(estaVacio(nuevaUnidad.marca, "marca"))
    handleValidationError(estaVacio(nuevaUnidad.modelo, "modelo"))
    handleValidationError(formatoPlaca(nuevaUnidad.placa))
    handleValidationError(anioValido(nuevaUnidad.anio))
    existe = vehicleRepository.obtenerPorPlaca(db, nuevaUnidad.placa)
    if existe is None:
        userService.obtener(db, nuevaUnidad.usuarioId)
        vehicle = vehicleRepository.crear(db, nuevaUnidad)
        return vehicle
    raise HTTPException(status_code=409, detail=f"La unidad con placa: {nuevaUnidad.placa} ya esta registrada.")

def obtener(db: Session, id:int):
    unidad = vehicleRepository.obtener(db, id)
    if unidad is None:
        raise HTTPException(status_code=404, detail="Unidad no encontrada.")
    return unidad

def obtenerTodos(db: Session):
    return vehicleRepository.obtenerTodos(db)

def actualizar(db: Session, id:int, nuevaUnidad: NuevaUnidad):
    handleValidationError(estaVacio(nuevaUnidad.marca, "marca"))
    handleValidationError(estaVacio(nuevaUnidad.modelo, "modelo"))
    handleValidationError(formatoPlaca(nuevaUnidad.placa))
    handleValidationError(anioValido(nuevaUnidad.anio))
    unidad = obtener(db, id)
    existe = vehicleRepository.obtenerPorPlaca(db, nuevaUnidad.placa)
    if existe is None or existe.id == unidad.id:
        userService.obtener(db, nuevaUnidad.usuarioId)
        unidad = vehicleRepository.actualizar(db, id, nuevaUnidad)
        return unidad
    raise HTTPException(status_code=409, detail=f"La unidad con placa: {nuevaUnidad.placa} ya esta registrada.")

def eliminar(db: Session, id:int):
    eliminado = vehicleRepository.eliminar(db, id)
    if eliminado is None:
        raise HTTPException(status_code=404, detail="Unidad no encontrada.")
    return True