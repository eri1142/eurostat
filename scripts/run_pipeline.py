import os
import shutil
from datetime import datetime
import subprocess

# Obtener el directorio actual donde se encuentra run_pipeline.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del intérprete de Python del entorno virtual
python_executable = os.path.join(current_dir, '..', 'env', 'Scripts', 'python.exe')

# Verifica si el intérprete existe
if not os.path.isfile(python_executable):
    raise FileNotFoundError(f"No se encontró el archivo {python_executable}")

# Paso 1: Ejecutar data_extraction.py
data_extraction_path = os.path.join(current_dir, 'data_extraction.py')
subprocess.run([python_executable, data_extraction_path], check=True)
print("data_extraction.py ejecutado correctamente.")

# Paso 2: Crear una carpeta con la fecha actual en formato YYYYMMDD en la ubicación correcta
fecha_actual = datetime.now().strftime('%Y%m%d')
historical_analysis_dir = os.path.join(current_dir, '..', 'notebooks', 'historical_analysis')
carpeta_destino = os.path.join(historical_analysis_dir, fecha_actual)

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Paso 3: Copiar el archivo data_analysis.ipynb con el nuevo nombre
data_analysis_path = os.path.join(current_dir, '..', 'notebooks', 'data_analysis.ipynb')
nombre_nuevo_notebook = f"data_analysis_{fecha_actual}.ipynb"
ruta_destino_notebook = os.path.join(carpeta_destino, nombre_nuevo_notebook)

if not os.path.isfile(data_analysis_path):
    raise FileNotFoundError(f"No se encontró el archivo {data_analysis_path}")

shutil.copy2(data_analysis_path, ruta_destino_notebook)

# Paso 4: Ejecutar el nuevo archivo data_analysis_YYYYMMDD.ipynb
# Ejecutar el notebook y guardar la salida
command = f"jupyter nbconvert --to notebook --execute --output {ruta_destino_notebook} {ruta_destino_notebook}"
subprocess.run(command, shell=True, check=True)

# Paso 5: Convertir el notebook a HTML usando Quarto
# Generar el archivo HTML en el mismo directorio
html_output_path = os.path.join(carpeta_destino, f"data_analysis_{fecha_actual}.html")
quarto_command = f"quarto convert {ruta_destino_notebook} --to html --output {html_output_path}"
subprocess.run(quarto_command, shell=True, check=True)

print(f"Notebook ejecutado y guardado en: {ruta_destino_notebook}")
