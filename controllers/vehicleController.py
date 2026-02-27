from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dbconnection import get_db
from services import vehicleService
from schemas.schemas import NuevaUnidad, Unidad
from controllers.globalExceptionHandler import global_exception_handler

router = APIRouter(prefix="/unidades", tags=["Unidades"])

@router.get("/", response_model=list[Unidad])
async def obtenerTodos(db: Session = Depends(get_db)):
    return vehicleService.obtenerTodos(db)

@router.get("/{id}", response_model=Unidad)
async def obtener(id:int, db: Session=Depends(get_db)):
    try:
        return vehicleService.obtener(db, id)
    except Exception as e:
        global_exception_handler(e)

@router.post("/", response_model=Unidad)
async def crear(nuevaUnidad: NuevaUnidad, db: Session = Depends(get_db)):
    try:
        unidad = vehicleService.crear(db, nuevaUnidad)
        return unidad
    except Exception as e:
        global_exception_handler(e)

@router.put("/{id}", response_model=Unidad)
async def actualizar(id:int, nuevaUnidad: NuevaUnidad, db: Session = Depends(get_db)):
    try:
        unidad = vehicleService.actualizar(db, id, nuevaUnidad)
        return unidad
    except Exception as e:
        global_exception_handler(e)

@router.delete("/{id}")
async def eliminar(id:int, db: Session = Depends(get_db)):
    try:
        vehicleService.eliminar(db, id)
    except Exception as e:
        global_exception_handler(e)