from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.schemas.receta_schema import CrearReceta, ResponsivoReceta
from app.services import receta_service

router = APIRouter(prefix="/recetas", tags=["Recetas"])

@router.get("", response_model=list[ResponsivoReceta])
def get_recetas(dificultad: str | None = None, db: Session = Depends(get_db)):
    return receta_service.listar_recetas(db, dificultad)

@router.get("/{receta_id}", response_model=ResponsivoReceta)
def get_receta(receta_id: int, db: Session = Depends(get_db)):
    return receta_service.obtener_receta(db, receta_id)

@router.post("", response_model=ResponsivoReceta, status_code=201)
def crear_receta(data: CrearReceta, db: Session = Depends(get_db)):
    return receta_service.registrar_receta(db, data)

@router.put("/{receta_id}", response_model=ResponsivoReceta)
def actualizar_receta(receta_id: int, data: CrearReceta, db: Session = Depends(get_db)):
    return receta_service.actualizar_receta(db, receta_id, data)

@router.delete("/{receta_id}")
def eliminar_receta(receta_id: int, db: Session = Depends(get_db)):
    return receta_service.eliminar_receta(db, receta_id)
