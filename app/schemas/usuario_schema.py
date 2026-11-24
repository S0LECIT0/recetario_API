from pydantic import BaseModel, ConfigDict, EmailStr, Field

class CrearUsuario(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    correo: EmailStr
    contrasena: str = Field(min_length=6, max_length=100)

class ResponsivoUsuario(BaseModel):
    id: int
    nombre: str
    correo: EmailStr

    model_config = ConfigDict(from_attributes=True)
