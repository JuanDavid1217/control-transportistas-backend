# Control Transportistas Backend
API REST creada con FastAPI para la gestion de usuarios y unidades de transporte.

## Características
Cuenta con los siguientes modulos:

- **Usuarios**: metodos POST, PUT, DELETE y GET.
- **Unidades**: metodos POST, PUT, DELETE y GET.
- **Rutas**:    metodos POST, PUT, DELETE y GET.
- **Metricas**: metodos POST, PUT, DELETE y GET.
- **Estatus**:  metodo GET.

## Estructura del proyecto
```
api/
├── main.py                         # Archivo principal para lanzar la API
├── dbconnection.py                 # Se establece la conexión con la base de datos
├── APIRouter.py                    # Permite una facil gestion de los controladores
├── controllers/
│   ├── globalExceptionHandler.py   # Manejador de Errores a nivel global
│   ├── metricsController.py        # Controlador para el modulo de rendimiento (metricas)
│   ├── routeController.py          # Controlador para el modulo de rutas
│   ├── statusController.py         # Controlador para el modulo de estatus
│   ├── userController.py           # Controlador para el modulo de usuarios
│   └── vehicleController.py        # Controlador para el modulo de unidades
├── models/
│   └── models.py                   # Realiza un mapeo directo contra la base de datos
├── repository/
│   ├── metricsRepository.py        # Acceso a datos para el rendimiento (metricas)
│   ├── routeRepository.py          # Acceso a datos para las rutas
│   ├── statusRepository.py         # Acceso a datos para los estados
│   ├── userRepository.py           # Acceso a datos para los usuarios
│   └── vehicleRepository.py        # Acceso a datos para las unidades (vehiculos)
├── schemas/
│   └── schemas.py                  # Formato de entrada y salida esperado para cada modulo (DTO)
├── services/
│   ├── metricsService.py           # Logica de negocio para la gestion del rendimiento (metricas)
│   ├── routeService.py             # Logica de negocio para la gestion de las rutas
│   ├── statusService.py            # Logica de negocio para la gestion de los estatus
│   ├── userService.py              # Logica de negocio para la gestion de los usuarios
│   └── vehicleService.py           # Logica de negocio para la gestion de las unidades (vehiculos)
```

## Instalación
1. Clona el repositorio
```
git clone https://github.com/JuanDavid1217/control-transportistas-backend 
```

2. Navega dentro de repositorio clonado
```
cd control-transportistas-backend
```

### Base de Datos (PostgreSQL)
1. Crea una Base de datos llamada `control-transportistas-db`

2. Ejecuta el contenido del script `control-transportistas-db.sql` (**Importante: El script borra inicialmente las tablas a utilizar si existen**)

### FastAPI
1. Navega a la carpeta `api` del repositorio clonado
```
cd api
```

2. Crea un entorno virtual
```
python -m venv venv
```

3. Activa el repositorio virtual
- Windows
```
.\venv\Scripts\activate
```

- Linux
```
source venv/bin/activate
```

4. Instala las librerias necesarias
```
python -m pip install -r requirements.txt
```

5. Crea un archivo .env con el siguiente contenido
**Nota:** Los valores aqui mostrados son los utilizados para probar en local, cambialos según lo requiera tu conexión. Recuerda no subir estos valores si son sensibles.

```
DATABASE_SERVICE=postgres
DATABASE_URL=postgresql://postgres:123456@localhost:5432/control-transportistas-db
```

6. Ejecuta el archivo principal
```
python -m main.py
```

## Uso
FastAPI maneja la documentación automatica mediante Swagger, para consultarla levanta la API en local y navega a `http://localhost:8000`, en atomatico te redirecionara a `/docs`.

## Tecnologías
- Base de datos con PostgreSQL
- Draw.io para el modelado de datos (diagrama relacional `control-transportistas-diagrama-relacional.drawio`)
- FastAPI
- SQLAlchemy

## Notas
- El campo email en usuarios debe ser unico.
- Para la creación de un nuevo vehiculo se valida que tenga asignado un usuario existente.
- La placa de cada unidad debe ser unica.
- Al crear una ruta se valida que el vehiculo asignado exista.
- El estatus por defecto de una ruta es "Asignada".
- Solo se permite iniciar ("En ruta") una ruta simpre y cuando este asignada.
- Solo se permite terminar ("Completada") una ruta siempre y cuando haya sido iniciada ("En ruta").
- Para editar y/o eliminar una ruta esta no debe de estar "Asignada" o "Completada".
- El rendimiento (metricas) solo se puede registrar cuando una ruta este "Completada", validando:
    - Que la ruta exista
    - Estatus de la ruta