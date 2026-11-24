from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Receta
from schemas import CrearReceta, ResponsivoReceta

Base.metadata.create_all(bind=engine)

app = FastAPI(title="recetario API")


@app.get("/receta", response_model=list[ResponsivoReceta])
def get_recetas(db: Session = Depends(get_db)):
    recetas = db.query(Receta).all()
    return recetas


@app.get("/receta/{receta_id}", response_model=ResponsivoReceta)
def get_receta(
    receta_id: int,
    db: Session = Depends(get_db),
):
    receta = db.query(Receta).filter(Receta.id == receta_id).first()

    if receta is None:
        raise HTTPException(
            status_code=404,
            detail="Receta no encontrada",
        )

    return receta


@app.post("/receta", response_model=ResponsivoReceta, status_code=201)
def crear_receta(
    data: CrearReceta,
    db: Session = Depends(get_db),
):
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


@app.put("/receta/{receta_id}", response_model=ResponsivoReceta)
def actualizar_receta(
    receta_id: int,
    data: CrearReceta,
    db: Session = Depends(get_db),
):
    receta = db.query(Receta).filter(Receta.id == receta_id).first()

    if receta is None:
        raise HTTPException(
            status_code=404,
            detail="Receta no encontrada",
        )

    receta.nombre = data.nombre
    receta.descripcion = data.descripcion
    receta.ingredientes = data.ingredientes
    receta.tiempo_preparacion = data.tiempo_preparacion
    receta.numero_porciones = data.numero_porciones
    receta.dificultad = data.dificultad

    db.commit()
    db.refresh(receta)

    return receta


@app.delete("/receta/{receta_id}")
def eliminar_receta(
    receta_id: int,
    db: Session = Depends(get_db),
):
    receta = db.query(Receta).filter(Receta.id == receta_id).first()

    if receta is None:
        raise HTTPException(
            status_code=404,
            detail="Receta no encontrada",
        )

    db.delete(receta)
    db.commit()

    return {"message": "Receta eliminada satisfactoriamente"}