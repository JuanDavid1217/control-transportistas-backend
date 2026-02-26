from pydantic import BaseModel, EmailStr
from datetime import datetime
from decimal import Decimal

class NuevoUsuario(BaseModel):
    nombe: str
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

class NuevaMetrica(BaseModel):
    distancia: Decimal
    combustible: Decimal

class Metrica(NuevaMetrica):
    id: int

    class Config:
        from_attributes = True

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
