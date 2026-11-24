from fastapi import FastAPI
from app.database.conexion import Base, engine
from app.routes import recetas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="recetario API")

app.include_router(recetas.router)
