# API de Gestión de Recetas de Cocina y Usuarios

**Aprendiz:** Marisol Andrea Loaiza Pérez  
**Ejercicio asignado:** Ejercicio 15 - API para gestión de recetas de cocina  
**Tecnologías:** Python, FastAPI, PostgreSQL (Neon), SQLAlchemy, Pydantic, Uvicorn  

---

## 1. Descripción del Proyecto
Este proyecto consiste en el desarrollo de una API REST utilizando FastAPI y PostgreSQL alojado en Neon. La aplicación permite gestionar un recetario de cocina (crear, listar, consultar por ID, actualizar, filtrar por dificultad y eliminar recetas) y cuenta además con un módulo independiente para la administración de usuarios con contraseñas seguras y validación de correos únicos.

## 2. Objetivo de la API
Construir una solución modular y escalable aplicando arquitectura en capas, que permita realizar operaciones CRUD completas y seguras a través de endpoints REST probados e interactivos desde Swagger UI.

---

## 3. Arquitectura en Capas

El proyecto está organizado respetando la separación de responsabilidades solicitada en la guía:

```text
recetario_API/
│
├── app/
│   ├── database/
│   │   └── conexion.py             # Conexión con la base de datos en Neon
│   ├── models/
│   │   ├── receta.py               # Modelo de la tabla receta
│   │   └── usuario.py              # Modelo de la tabla usuario
│   ├── schemas/
│   │   ├── receta_schema.py        # Validaciones de entrada y salida de recetas
│   │   └── usuario_schema.py       # Validaciones de entrada y salida de usuarios
│   ├── repositories/
│   │   ├── receta_repository.py    # Consultas SQL para recetas
│   │   └── usuario_repository.py   # Consultas SQL para usuarios
│   ├── services/
│   │   ├── receta_service.py       # Lógica del negocio para recetas
│   │   └── usuario_service.py      # Lógica de usuarios (hashing y correos únicos)
│   └── routes/
│       ├── recetas.py              # Endpoints HTTP de recetas
│       └── usuarios.py             # Endpoints HTTP de usuarios
│
├── main.py                         # Inicialización y registro de rutas de FastAPI
├── requirements.txt                # Dependencias instaladas
├── .env                            # Variables de entorno (credenciales Neon)
└── .gitignore
```

### Responsabilidad de cada capa:
- **Routes:** Define las rutas (endpoints), recibe las peticiones HTTP del cliente y retorna las respuestas.
- **Services:** Contiene la lógica del negocio (validar que el correo no esté repetido, hashear la contraseña, etc.).
- **Repositories:** Interactúa directamente con la base de datos a través de SQLAlchemy para hacer las consultas y cambios.
- **Models:** Define las tablas en PostgreSQL con sus columnas y tipos de datos.
- **Schemas:** Valida los datos que entran y salen usando Pydantic.
- **Database:** Administra la conexión a PostgreSQL en Neon mediante la variable de entorno `DATABASE_URL`.

---

## 4. Tablas de la Base de Datos

### Tabla: `receta`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Integer (PK) | Identificador único autoincremental |
| `nombre` | String(100) | Nombre del platillo o receta |
| `descripcion` | String(500) | Descripción de la receta |
| `ingredientes` | String(500) | Lista de ingredientes |
| `tiempo_preparacion` | Time | Tiempo estimado de preparación |
| `numero_porciones` | Integer | Número de porciones (> 0) |
| `dificultad` | String(20) | Dificultad (ej: Fácil, Media, Difícil) |

### Tabla: `usuario`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Integer (PK) | Identificador único autoincremental |
| `nombre` | String(100) | Nombre completo del usuario |
| `correo` | String(100) | Correo electrónico único |
| `contrasena` | String(255) | Contraseña almacenada en hash (no texto plano) |

---

## 5. Endpoints Implementados

### Módulo de Recetas (`/recetas`)
- `POST /recetas`: Registrar una nueva receta.
- `GET /recetas`: Consultar todas las recetas.
- `GET /recetas?dificultad={valor}`: **Filtro por dificultad** (ej: `/recetas?dificultad=Fácil`).
- `GET /recetas/{receta_id}`: Consultar una receta por su ID.
- `PUT /recetas/{receta_id}`: Actualizar la información de una receta.
- `DELETE /recetas/{receta_id}`: Eliminar una receta.

### Módulo de Usuarios (`/usuarios`)
- `POST /usuarios`: Registrar usuario (valida campos obligatorios, evita correos duplicados y guarda contraseña hasheada).
- `GET /usuarios`: Consultar todos los usuarios (no expone las contraseñas).
- `GET /usuarios/{id}`: Consultar un usuario por ID.
- `PUT /usuarios/{id}`: Actualizar la información del usuario.
- `DELETE /usuarios/{id}`: Eliminar un usuario.

---

## 6. Pruebas y Uso en Swagger UI

1. Para iniciar el servidor de desarrollo:
   ```bash
   uvicorn main:app --reload
   ```
2. Abrir en el navegador:
   `http://127.0.0.1:8000/docs`
3. Desde la interfaz interactiva de Swagger se pueden probar todas las operaciones CRUD tanto de recetas como de usuarios.

---

## 7. Despliegue y Conexión

- **Neon:** Se configuró una base de datos PostgreSQL en la nube de Neon y la cadena de conexión se maneja de forma segura en el archivo `.env`.
- **GitHub:** Repositorio con el código estructurado en capas, `.gitignore` para no subir `.env` ni carpetas innecesarias.
- **Render:** Despliegue mediante Web Service vinculado al repositorio de GitHub con el comando `uvicorn main:app --host 0.0.0.0 --port $PORT`.
