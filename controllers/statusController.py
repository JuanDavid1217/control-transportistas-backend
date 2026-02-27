from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dbconnection import get_db
from services import statusService
from schemas.schemas import Estatus
from controllers.globalExceptionHandler import global_exception_handler

router = APIRouter(prefix="/estatus", tags=["Estatus"])

@router.get("/", response_model=list[Estatus])
async def obtenerTodos(db: Session = Depends(get_db)):
    return statusService.obtenerTodos(db)

@router.get("/{id}", response_model=Estatus)
async def obtener(id:int, db: Session=Depends(get_db)):
    try:
        return statusService.obtener(db, id)
    except Exception as e:
        global_exception_handler(e)

