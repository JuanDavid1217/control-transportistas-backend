from pydantic import BaseModel, EmailStr
from datetime import datetime
from decimal import Decimal
from utils.durationFormatter import timedeltaAString

class NuevoUsuario(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str

class Usuario(NuevoUsuario):
    id: int
    fechaCreacion: datetime

    class Config:
        from_attributes = True

class UnidadBase(BaseModel):
    placa: str
    marca: str
    modelo: str
    anio: int

class NuevaUnidad(UnidadBase):
    usuarioId: int

class Unidad(UnidadBase):
    id: int
    usuario: Usuario
    fechaCreacion: datetime

    class Config:
        from_attributes = True


class NuevoEstatus(BaseModel):
    nombre: str

class Estatus(NuevoEstatus):
    id: int

    class Config:
        from_attributes = True

class MetricaBase(BaseModel):
    distancia: Decimal
    combustible: Decimal

class NuevaMetrica(MetricaBase):
    id: int

class Metrica(NuevaMetrica):
    duracion: str

    class Config:
        from_attributes = True
    
    @classmethod
    def from_orm(cls, obj):
        if obj:
            return cls(
                id=obj.id,
                distancia=obj.distancia,
                combustible=obj.combustible,
                duracion = timedeltaAString(obj.duracion)
            )

class NuevaRuta(BaseModel):
    unidadId: int
    inicio: str
    destino: str

class Ruta(NuevaRuta):
    id: int
    estatus: Estatus
    horaInicio: datetime | None = None
    horaFin: datetime | None = None
    unidad: Unidad
    metrica: Metrica | None = None

    class Config:
        from_attributes = True
    
    @classmethod
    def from_orm(cls, obj):
        if obj:
            return cls(
                id= obj.id,
                estatus= obj.estatus,
                horaInicio= obj.horaInicio,
                horaFin= obj.horaFin,
                unidad= obj.unidad,
                metrica= Metrica.from_orm(obj.metrica),
                unidadId = obj.unidadId,
                inicio = obj.inicio,
                destino = obj.destino
            )
