from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dbconnection import get_db
from services import metricsService
from schemas.schemas import NuevaMetrica, Metrica
from controllers.globalExceptionHandler import global_exception_handler

router = APIRouter(prefix="/metricas", tags=["Metricas"])

@router.get("/", response_model=list[Metrica])
async def obtenerTodos(db: Session = Depends(get_db)):
    return metricsService.obtenerTodos(db)

@router.get("/{id}", response_model=Metrica)
async def obtener(id:int, db: Session=Depends(get_db)):
    try:
        return metricsService.obtener(db, id)
    except Exception as e:
        global_exception_handler(e)

@router.post("/", response_model=Metrica)
async def crear(nuevaMetrica: Metrica, db: Session = Depends(get_db)):
    try:
        metrica = metricsService.crear(db, nuevaMetrica)
        return metrica
    except Exception as e:
        global_exception_handler(e)

@router.put("/{id}", response_model=Metrica)
async def actualizar(id:int, nuevaMetrica: NuevaMetrica, db: Session = Depends(get_db)):
    try:
        ruta = metricsService.actualizar(db, id, nuevaMetrica)
        return ruta
    except Exception as e:
        global_exception_handler(e)

@router.delete("/{id}")
async def eliminar(id:int, db: Session = Depends(get_db)):
    try:
        metricsService.eliminar(db, id)
    except Exception as e:
        global_exception_handler(e)
