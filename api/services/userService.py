from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import NuevoUsuario
from repository import userRepository

def crear(db: Session, nuevoUsuario: NuevoUsuario):
    existe = userRepository.obtenerPorEmail(db, nuevoUsuario.email)
    if existe is None:
        usuario = userRepository.crear(db, nuevoUsuario)
        return usuario
    raise HTTPException(status_code=409, detail=f"El email: {nuevoUsuario.email} ya esta registrado.")

def obtener(db: Session, id:int):
    usuario = userRepository.obtener(db, id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return usuario

def obtenerTodos(db: Session):
    return userRepository.obtenerTodos(db)

def actualizar(db: Session, id:int, nuevoUsuario: NuevoUsuario):
    usuario = obtener(db, id)
    existe = userRepository.obtenerPorEmail(db, nuevoUsuario.email)
    if existe is None or existe.id == usuario.id:
        usuario = userRepository.actualizar(db, id, nuevoUsuario)
        return usuario
    raise HTTPException(status_code=409, detail=f"El email: {nuevoUsuario.email} ya esta registrado.")

def eliminar(db: Session, id:int):
    eliminado = userRepository.eliminar(db, id)
    if eliminado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return True