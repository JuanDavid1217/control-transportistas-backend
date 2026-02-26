from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def crear(db: Session, nuevoUsuario: schemas.NuevoUsuario):
    try:
        usuario = models.Usuario(nombre=nuevoUsuario.nombre, email=nuevoUsuario.email, telefono=nuevoUsuario.telefono)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as e:
        db.rollback()
        raise e

def obtener(db: Session, id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    return usuario

def obtenerTodos(db: Session):
    usuarios = db.query(models.Usuario).all()
    return usuarios

def actualizar(db: Session, id:int, nuevoUsuario: schemas.NuevoUsuario):
    usuario = obtener(db, id)
    if usuario:
        try:
            usuario.nombre = nuevoUsuario.nombre
            usuario.email = nuevoUsuario.email
            usuario.telefono = nuevoUsuario.telefono
            db.commit()
            db.refresh(usuario)
            return usuario
        except Exception as e:
            db.rollback()
            raise e
    return None

def eliminar(db: Session, id: int):
    usuario = obtener(db, id)
    if usuario:
        try:
            db.delete(usuario)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            raise e
    return None
