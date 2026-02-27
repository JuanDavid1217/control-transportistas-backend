from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dbconnection import get_db
from services import userService
from schemas.schemas import NuevoUsuario, Usuario
from controllers.globalExceptionHandler import global_exception_handler

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/", response_model=list[Usuario])
async def obtenerTodos(db: Session = Depends(get_db)):
    return userService.obtenerTodos(db)

@router.get("/{id}", response_model=Usuario)
async def obtener(id:int, db: Session=Depends(get_db)):
    try:
        return userService.obtener(db, id)
    except Exception as e:
        global_exception_handler(e)

@router.post("/", response_model=Usuario)
async def crear(nuevoUsuario: NuevoUsuario, db: Session = Depends(get_db)):
    try:
        usuario = userService.crear(db, nuevoUsuario)
        return usuario
    except Exception as e:
        global_exception_handler(e)

@router.put("/{id}", response_model=Usuario)
async def actualizar(id:int, nuevoUsuario: NuevoUsuario, db: Session = Depends(get_db)):
    try:
        usuario = userService.actualizar(db, id, nuevoUsuario)
        return usuario
    except Exception as e:
        global_exception_handler(e)

@router.delete("/{id}")
async def eliminar(id:int, db: Session = Depends(get_db)):
    try:
        userService.eliminar(db, id)
    except Exception as e:
        global_exception_handler(e)