# Eurostat Data Extraction and Analysis

Este proyecto está diseñado para extraer y analizar datos desde la API de Eurostat, específicamente utilizando la clasificación COICOP para el análisis de índices de precios al consumidor (HICP).

## Estructura del Proyecto

```
Eurostat/
│
├── datafilecsv/        # Carpeta que contiene los archivos CSV descargados desde Eurostat
├── env/                # Entorno virtual de Python con las dependencias del proyecto
├── main.py             # Script principal que realiza la extracción y tratamiento de datos
└── README.md           # Archivo de documentación del proyecto
```

### Archivos y Directorios

- **`datafilecsv/`**: Este directorio contiene los archivos CSV generados durante la ejecución del script `main.py`. Estos archivos son exportaciones de datos obtenidos desde la API de Eurostat.

- **`env/`**: Este directorio contiene el entorno virtual de Python utilizado para este proyecto. Todas las dependencias necesarias están instaladas aquí para asegurar un entorno reproducible.

- **`main.py`**: Este es el archivo principal que contiene el código para extraer datos desde la API de Eurostat, procesarlos y almacenarlos en formato CSV. 

- **`README.md`**: Archivo de documentación que explica la estructura del proyecto, su propósito y cómo utilizarlo.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado Python 3.7 o superior y de haber creado un entorno virtual con las dependencias necesarias. Puedes hacerlo ejecutando:

```bash
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
pip install -r requirements.txt
```

## Uso

1. **Activar el entorno virtual**: 
   ```bash
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

2. **Ejecutar el script principal**:
   ```bash
   python main.py
   ```

3. **Explorar los datos**:
   Los archivos CSV generados estarán disponibles en la carpeta `datafilecsv/`.

## Explicación del Código

### `main.py`

El script `main.py` realiza las siguientes funciones principales:

1. **Importación de Librerías**:
   - Se importan librerías como `requests`, `pandas`, `os`, y `datetime` para manejar la solicitud a la API, manipulación de datos, y gestión de archivos.

2. **Obtención de la Fecha Actual**:
   - Se utiliza `datetime` para obtener la fecha actual y formatearla en `DD-MM-YYYY`, que es útil para nombrar los archivos generados o para incluir esta información en los datos.

3. **Función `explore_json(data)`**:
   - Esta función recursiva permite explorar la estructura de un JSON. Es útil para entender cómo está estructurada la respuesta de una API antes de procesarla.

4. **Definición de `coicop_codes`**:
   - Una lista de diccionarios que mapea la clasificación COICOP a sus respectivos códigos. Esto se utiliza para realizar consultas específicas a la API de Eurostat.

5. **Extracción y Tratamiento de Datos**:
   - Se realiza una solicitud a la API de Eurostat usando los códigos COICOP y se procesan los datos recibidos. Estos datos se exportan en formato CSV dentro de la carpeta `datafilecsv`.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o deseas mejorar el código, siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, revisa el archivo `LICENSE`.
