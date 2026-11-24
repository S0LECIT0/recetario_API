import hashlib
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from app.database.conexion import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)

    @validates("contrasena")
    def cifrar_contrasena(self, key, value):
        if value and not (len(value) == 64 and all(c in "0123456789abcdefABCDEF" for c in value)):
            return hashlib.sha256(value.encode()).hexdigest()
        return value
