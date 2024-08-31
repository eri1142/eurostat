import subprocess
import papermill as pm
import os

def run_main_script():
    """Ejecuta el script principal y captura la salida."""
    result = subprocess.run(['python', 'scripts/data_extraction.py'], capture_output=True, text=True)
    output_file = result.stdout.strip()
    return output_file

def run_eda_notebook(csv_file):
    """Ejecuta el notebook de EDA usando papermill."""
    pm.execute_notebook(
        'notebooks/data_analysis.ipynb',  # Path al notebook EDA
        'notebooks/data_analysis_output.ipynb',  # Output del notebook ejecutado
        parameters=dict(csv_file=csv_file)
    )

def main():
    """Función principal para ejecutar el pipeline completo."""
    output_file = run_main_script()
    
    if os.path.exists(output_file):
        run_eda_notebook(output_file)
    else:
        print(f"Error: El archivo {output_file} no se encontró.")

if __name__ == "__main__":
    main()
