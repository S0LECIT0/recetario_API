from sqlalchemy.orm import Session
from app.models.receta import Receta
from app.schemas.receta_schema import CrearReceta

def obtener_recetas(db: Session):
    return db.query(Receta).all()

def obtener_receta_por_id(db: Session, receta_id: int):
    return db.query(Receta).filter(Receta.id == receta_id).first()

def crear_receta(db: Session, data: CrearReceta):
    receta = Receta(
        nombre=data.nombre,
        descripcion=data.descripcion,
        ingredientes=data.ingredientes,
        tiempo_preparacion=data.tiempo_preparacion,
        numero_porciones=data.numero_porciones,
        dificultad=data.dificultad,
    )
    db.add(receta)
    db.commit()
    db.refresh(receta)
    return receta

def actualizar_receta(db: Session, receta: Receta, data: CrearReceta):
    receta.nombre = data.nombre
    receta.descripcion = data.descripcion
    receta.ingredientes = data.ingredientes
    receta.tiempo_preparacion = data.tiempo_preparacion
    receta.numero_porciones = data.numero_porciones
    receta.dificultad = data.dificultad
    db.commit()
    db.refresh(receta)
    return receta

def eliminar_receta(db: Session, receta: Receta):
    db.delete(receta)
    db.commit()
