from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import NuevaUnidad
from repository import vehicleRepository

def crear(db: Session, nuevaUnidad: NuevaUnidad):
    existe = vehicleRepository.obtenerPorPlaca(db, nuevaUnidad.placa)
    if existe is None:
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
    unidad = obtener(db, id)
    existe = vehicleRepository.obtenerPorPlaca(db, nuevaUnidad.placa)
    if existe is None or existe.id == unidad.id:
        unidad = vehicleRepository.actualizar(db, id, nuevaUnidad)
        return unidad
    raise HTTPException(status_code=409, detail=f"La unidad con placa: {nuevaUnidad.placa} ya esta registrada.")

def eliminar(db: Session, id:int):
    eliminado = vehicleRepository.eliminar(db, id)
    if eliminado is None:
        raise HTTPException(status_code=404, detail="Unidad no encontrada.")
    return True