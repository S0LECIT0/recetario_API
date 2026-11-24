from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import receta_repository
from app.schemas.receta_schema import CrearReceta

def listar_recetas(db: Session, dificultad: str | None = None):
    return receta_repository.obtener_recetas(db, dificultad)

def obtener_receta(db: Session, receta_id: int):
    receta = receta_repository.obtener_receta_por_id(db, receta_id)
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    return receta

def registrar_receta(db: Session, data: CrearReceta):
    return receta_repository.crear_receta(db, data)

def actualizar_receta(db: Session, receta_id: int, data: CrearReceta):
    receta = obtener_receta(db, receta_id)
    return receta_repository.actualizar_receta(db, receta, data)

def eliminar_receta(db: Session, receta_id: int):
    receta = obtener_receta(db, receta_id)
    receta_repository.eliminar_receta(db, receta)
    return {"message": "Receta eliminada satisfactoriamente"}
