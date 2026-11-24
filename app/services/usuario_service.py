import hashlib
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import usuario_repository
from app.schemas.usuario_schema import CrearUsuario

def hashear_contrasena(contrasena: str):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def listar_usuarios(db: Session):
    return usuario_repository.obtener_usuarios(db)

def obtener_usuario(db: Session, usuario_id: int):
    usuario = usuario_repository.obtener_usuario_por_id(db, usuario_id)
    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado",
        )
    return usuario

def registrar_usuario(db: Session, data: CrearUsuario):
    usuario_existente = usuario_repository.obtener_usuario_por_correo(db, data.correo)
    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="El correo ya se encuentra registrado",
        )
    
    contrasena_hash = hashear_contrasena(data.contrasena)
    return usuario_repository.crear_usuario(db, data, contrasena_hash)

def actualizar_usuario(db: Session, usuario_id: int, data: CrearUsuario):
    usuario = obtener_usuario(db, usuario_id)

    usuario_con_correo = usuario_repository.obtener_usuario_por_correo(db, data.correo)
    if usuario_con_correo and usuario_con_correo.id != usuario_id:
        raise HTTPException(
            status_code=400,
            detail="El correo ya se encuentra registrado",
        )

    contrasena_hash = hashear_contrasena(data.contrasena)
    return usuario_repository.actualizar_usuario(db, usuario, data, contrasena_hash)

def eliminar_usuario(db: Session, usuario_id: int):
    usuario = obtener_usuario(db, usuario_id)
    usuario_repository.eliminar_usuario(db, usuario)
    return {"message": "Usuario eliminado satisfactoriamente"}
