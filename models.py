from sqlalchemy import Column, Integer, String, Time
from database import Base

class Receta(Base):

    __tablename__ = "receta"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=False)
    ingredientes = Column(String(500), nullable=False)
    tiempo_preparacion = Column(Time, nullable=False)
    numero_porciones = Column(Integer, nullable=False)
    dificultad = Column(String(20), nullable=False)