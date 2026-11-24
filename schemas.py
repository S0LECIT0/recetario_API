from datetime import time
from pydantic import BaseModel, ConfigDict, Field

class CrearReceta(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str = Field(min_length=2, max_length=500)
    ingredientes: str = Field(min_length=2, max_length=100)
    tiempo_preparacion = time
    numero_porciones = int = Field(gt=0)

class ResponsivoReceta(BaseModel):
    id: int
    nombre: str
    descripcion: str
    ingredientes: str
    tiempo_preparacion: time
    numero_pociones: int