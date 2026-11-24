from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.schemas.usuario_schema import CrearUsuario, ResponsivoUsuario
from app.services import usuario_service

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("", response_model=list[ResponsivoUsuario])
def get_usuarios(db: Session = Depends(get_db)):
    return usuario_service.listar_usuarios(db)

@router.get("/{id}", response_model=ResponsivoUsuario)
def get_usuario(id: int, db: Session = Depends(get_db)):
    return usuario_service.obtener_usuario(db, id)

@router.post("", response_model=ResponsivoUsuario, status_code=201)
def crear_usuario(data: CrearUsuario, db: Session = Depends(get_db)):
    return usuario_service.registrar_usuario(db, data)

@router.put("/{id}", response_model=ResponsivoUsuario)
def actualizar_usuario(id: int, data: CrearUsuario, db: Session = Depends(get_db)):
    return usuario_service.actualizar_usuario(db, id, data)

@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    return usuario_service.eliminar_usuario(db, id)
