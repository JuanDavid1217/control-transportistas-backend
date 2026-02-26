from sqlalchemy import Column, ForeignKey, BigInteger, String, SmallInteger, Numeric, Text, DateTime, func, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Usuario(Base):
    __tablename__="Usuarios"
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telefono = Column(String(10), nullable=False)
    fechaCreacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    unidades = relationship("Unidad", back_populates="usuario", cascade="all, delete")

class Unidad(Base):
    __tablename__="Unidades"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    placa= Column(String(15), unique=True, nullable=False)
    marca= Column(String(100), nullable=False)
    modelo= Column(String(100), nullable=False)
    anio= Column(SmallInteger, nullable=False)
    usuarioId= Column( BigInteger, ForeignKey("Usuarios.id", ondelete="CASCADE"), nullable=False)
    fechaCreacion= Column( DateTime(timezone=True), server_default=func.now())

    usuario = relationship("Usuario", back_populates="unidades", uselist=False)
    rutas = relationship("Ruta", back_populates="unidad", cascade="all, delete")

class Estatus(Base):
    __tablename__ = "Estatus"

    id= Column(SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(50), unique=True, nullable=False)

    rutas = relationship("Ruta", back_populates="estatus")


class Ruta(Base):
    __tablename__ = "Rutas"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=True)
    unidadId = Column(BigInteger, ForeignKey("Unidades.id", ondelete="CASCADE"), nullable=False)
    inicio = Column(Text, nullable=False)
    destino = Column(Text, nullable=False)
    estatusId = Column(SmallInteger, ForeignKey("Estatus.id"), nullable=False, server_default=text("1"))
    horaInicio = Column(DateTime(timezone=True))
    horaFin = Column(DateTime(timezone=True))

    unidad = relationship("Unidad", back_populates="rutas", uselist=False)
    estatus = relationship("Estatus", back_populates="rutas", uselist=False)
    metrica = relationship("MetricaPorRuta", back_populates="ruta", uselist=False)

class MetricaPorRuta(Base):
    __tablename__ = "MetricasPorRuta"
    
    id = Column(BigInteger, ForeignKey("Rutas.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    distancia = Column(Numeric(10, 2), nullable=False)
    combustible = Column(Numeric(10, 2), nullable=False)

    ruta = relationship("Ruta", back_populates="metrica")