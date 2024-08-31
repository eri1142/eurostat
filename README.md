# Eurostat Data Extraction and Analysis

Este proyecto está diseñado para extraer y analizar datos desde la API de Eurostat, específicamente utilizando la clasificación COICOP para el análisis de índices de precios al consumidor (HICP).

## Estructura del Proyecto

```
C:\DataAnalysis\Eurostat\
│
├── env\                        # Entorno virtual de Python
│   ├── Scripts\
│   │   └── python.exe          # Intérprete de Python
│   └── ...                     # Otros archivos del entorno virtual
│
├── notebooks\
│   ├── historical_analysis\    # Carpeta para notebooks históricos
│   │   └── YYYYMMDD\           # Carpeta para notebooks de fecha específica
│   └── data_analysis.ipynb     # Notebook principal a ejecutar y copiar
│
├── scripts\
│   ├── run_pipeline.py         # Script principal que ejecuta el pipeline
│   └── data_extraction.py      # Script para extracción de datos
│
├── datafilecsv\                # Carpeta para archivos CSV generados
│   └── prc_hicp_manr_31-08-2024.csv
│
└── latest_output.txt           # Archivo TXT para el archivo de salida más reciente

```


### Archivos y Directorios

- **`env/`**: Este directorio contiene el entorno virtual de Python utilizado para el proyecto. Todas las dependencias necesarias están instaladas aquí para asegurar un entorno reproducible.

- **`notebooks/`**:
  - **`historical_analysis/`**: Carpeta para almacenar los notebooks históricos de análisis. Cada subcarpeta dentro de esta carpeta está nombrada con la fecha en formato `YYYYMMDD`.
  - **`data_analysis.ipynb`**: Notebook principal que se copia y ejecuta en la carpeta `historical_analysis` con un nombre que incluye la fecha actual.

- **`scripts/`**:
  - **`run_pipeline.py`**: Script principal que coordina la ejecución de `data_extraction.py`, la creación de carpetas y la ejecución del notebook `data_analysis.ipynb`.
  - **`data_extraction.py`**: Script encargado de la extracción de datos desde la API de Eurostat y el almacenamiento de archivos CSV.

- **`datafilecsv/`**: Carpeta que contiene los archivos CSV generados durante la ejecución del script `data_extraction.py`.

- **`latest_output.txt`**: Archivo de texto que contiene información sobre el archivo de salida más reciente generado.

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
   python scripts/run_pipeline.py
   ```

3. **Explorar los datos**:
   Los archivos CSV generados estarán disponibles en la carpeta `datafilecsv/`.
   Los notebook de Jupyter generados estarán disponibles en la carpeta `notebooks/historical_analysis\YYYYMMDD`.

## Explicación del Código

### `scripts/run_pipeline.py`

El script `run_pipeline.py` realiza las siguientes funciones principales:

1. **Importación de Librerías**:
   - Se importan librerías como `os`, `shutil`, `datetime` y `subprocess` para manejar la gestión de archivos, la fecha y la ejecución de scripts externos.

2. **Ejecución de `data_extraction.py`**:
   - Se ejecuta el script `data_extraction.py` que extrae datos desde la API de Eurostat y guarda archivos CSV en `datafilecsv/`.

3. **Creación de Carpeta para Notebooks Históricos**:
   - Se crea una carpeta con la fecha actual en formato `YYYYMMDD` dentro de `notebooks/historical_analysis`.

4. **Copia y Ejecución del Notebook**:
   - Se copia el notebook `data_analysis.ipynb` a la nueva carpeta con la fecha actual y se ejecuta usando `jupyter nbconvert`.

### `scripts/data_extraction.py`

Este script realiza las siguientes funciones:

1. **Extracción de Datos**:
   - Se extraen datos desde la API de Eurostat y se guardan en archivos CSV en `datafilecsv/`.

2. **Actualización del Archivo TXT**:
   - Se actualiza `latest_output.txt` con la información del archivo CSV más reciente.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o deseas mejorar el código, siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, revisa el archivo `LICENSE`.

### Resumen de Cambios

1. **Estructura del Proyecto**: Se incluye la estructura de directorios y archivos del proyecto en formato de árbol.
2. **Descripción de Archivos y Directorios**: Se proporciona una explicación detallada de cada directorio y archivo en el proyecto.
3. **Instrucciones de Uso**: Incluye cómo activar el entorno virtual y ejecutar los scripts.
4. **Explicación del Código**: Se explica el propósito de los scripts principales y sus funciones.

Este README.md actualizado debe proporcionar una visión clara y completa de la estructura y uso del proyecto.

