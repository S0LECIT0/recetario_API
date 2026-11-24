from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario_schema import CrearUsuario

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()

def crear_usuario(db: Session, data: CrearUsuario, contrasena_hash: str):
    usuario = Usuario(
        nombre=data.nombre,
        correo=data.correo,
        contrasena=contrasena_hash,
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def actualizar_usuario(db: Session, usuario: Usuario, data: CrearUsuario, contrasena_hash: str):
    usuario.nombre = data.nombre
    usuario.correo = data.correo
    usuario.contrasena = contrasena_hash
    db.commit()
    db.refresh(usuario)
    return usuario

def eliminar_usuario(db: Session, usuario: Usuario):
    db.delete(usuario)
    db.commit()
