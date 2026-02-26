from sqlalchemy.orm import Session
from models.models import Usuario
from schemas.schemas import NuevoUsuario

def crear(db: Session, nuevoUsuario: NuevoUsuario):
    try:
        usuario = Usuario(nombre=nuevoUsuario.nombre, email=nuevoUsuario.email, telefono=nuevoUsuario.telefono)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as e:
        db.rollback()
        raise e

def obtener(db: Session, id: int):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    return usuario

def obtenerTodos(db: Session):
    usuarios = db.query(Usuario).all()
    return usuarios

def obtenerPorEmail(db:Session, email:str):
    usuario = db.query(Usuario).filter(Usuario.email==email).first()
    return usuario

def actualizar(db: Session, id:int, nuevoUsuario: NuevoUsuario):
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
