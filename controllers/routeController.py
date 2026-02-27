from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dbconnection import get_db
from services import routeService
from schemas.schemas import NuevaRuta, Ruta
from controllers.globalExceptionHandler import global_exception_handler

router = APIRouter(prefix="/rutas", tags=["Rutas"])

@router.get("/", response_model=list[Ruta])
async def obtenerTodos(db: Session = Depends(get_db)):
    return routeService.obtenerTodos(db)

@router.get("/{id}", response_model=Ruta)
async def obtener(id:int, db: Session=Depends(get_db)):
    try:
        return routeService.obtener(db, id)
    except Exception as e:
        global_exception_handler(e)

@router.post("/", response_model=Ruta)
async def crear(nuevaRuta: NuevaRuta, db: Session = Depends(get_db)):
    try:
        ruta = routeService.crear(db, nuevaRuta)
        return ruta
    except Exception as e:
        global_exception_handler(e)

@router.put("/{id}", response_model=Ruta)
async def actualizar(id:int, nuevaRuta: NuevaRuta, db: Session = Depends(get_db)):
    try:
        ruta = routeService.actualizar(db, id, nuevaRuta)
        return ruta
    except Exception as e:
        global_exception_handler(e)

@router.delete("/{id}")
async def eliminar(id:int, db: Session = Depends(get_db)):
    try:
        routeService.eliminar(db, id)
    except Exception as e:
        global_exception_handler(e)

@router.patch("/{id}/iniciar", response_model=Ruta)
async def iniciar(id: int, db: Session = Depends(get_db)):
    try:
        ruta = routeService.iniciar(db, id)
        return ruta
    except Exception as e:
        global_exception_handler(e)

@router.patch("/{id}/completar", response_model=Ruta)
async def completar(id: int, db: Session = Depends(get_db)):
    try:
        ruta = routeService.completar(db, id)
        return ruta
    except Exception as e:
        global_exception_handler(e)