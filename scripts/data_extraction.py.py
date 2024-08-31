# Chat GPT: https://chatgpt.com/share/d7bdea30-8ec0-457a-8f4b-9343716b5023


# Importar librerias
import requests
import pandas as pd
import os



# Obtener datetime de ejecución
from datetime import datetime 
fecha_actual = datetime.now().strftime("%d-%m-%Y") #Formatear fecha DD/MM/YYYY


def explore_json(data, level=0):
    """
    Esta función imprimirá las claves de todos los niveles del JSON y te dará una idea de la estructura completa.
    """
    if isinstance(data, dict):
        for key in data:
            print(' ' * (level * 4) + f"Clave: {key}")
            explore_json(data[key], level + 1)
    elif isinstance(data, list):
        print(' ' * (level * 4) + f"Lista con {len(data)} elementos")
        for item in data[:1]:  # Limitar a explorar solo el primer elemento en listas largas
            explore_json(item, level + 1)
    else:
        print(' ' * (level * 4) + f"Valor: {data}")



# Definimos la tabla coicop_codes

coicop_codes = [
    {"_ClassificationCOICOP": "All-items HICP", "_CodeIDCOICOP": "CP00"},
    {"_ClassificationCOICOP": "Food and non-alcoholic beverages", "_CodeIDCOICOP": "CP01"},
    {"_ClassificationCOICOP": "Alcoholic beverages, tobacco and narcotics", "_CodeIDCOICOP": "CP02"},
    {"_ClassificationCOICOP": "Clothing and footwear", "_CodeIDCOICOP": "CP03"},
    {"_ClassificationCOICOP": "Housing, water, electricity, gas and other fuels", "_CodeIDCOICOP": "CP04"},
    {"_ClassificationCOICOP": "Furnishings, household equipment and routine household maintenance", "_CodeIDCOICOP": "CP05"},
    {"_ClassificationCOICOP": "Health", "_CodeIDCOICOP": "CP06"},
    {"_ClassificationCOICOP": "Transport", "_CodeIDCOICOP": "CP07"},
    {"_ClassificationCOICOP": "Communications", "_CodeIDCOICOP": "CP08"},
    {"_ClassificationCOICOP": "Recreation and culture", "_CodeIDCOICOP": "CP09"},
    {"_ClassificationCOICOP": "Education", "_CodeIDCOICOP": "CP10"},
    {"_ClassificationCOICOP": "Restaurants and hotels", "_CodeIDCOICOP": "CP11"},
    {"_ClassificationCOICOP": "Miscellaneous goods and services", "_CodeIDCOICOP": "CP12"},
    {"_ClassificationCOICOP": "Food including alcohol and tobacco", "_CodeIDCOICOP": "FOOD"},
]


# Definimos la tabla geo_codes

geo_codes = [
    {"_NameGeo": "Belgium", "_CodeGeo": "BE"},
    {"_NameGeo": "Germany", "_CodeGeo": "DE"},
    {"_NameGeo": "Estonia", "_CodeGeo": "EE"},
    {"_NameGeo": "Ireland", "_CodeGeo": "IE"},
    {"_NameGeo": "Greece", "_CodeGeo": "GR"},
    {"_NameGeo": "Spain", "_CodeGeo": "ES"},
    {"_NameGeo": "France", "_CodeGeo": "FR"},
    {"_NameGeo": "Croatia", "_CodeGeo": "HR"},
    {"_NameGeo": "Italy", "_CodeGeo": "IT"},
    {"_NameGeo": "Cyprus", "_CodeGeo": "CY"},
    {"_NameGeo": "Latvia", "_CodeGeo": "LV"},
    {"_NameGeo": "Lithuania", "_CodeGeo": "LT"},
    {"_NameGeo": "Luxembourg", "_CodeGeo": "LU"},
    {"_NameGeo": "Malta", "_CodeGeo": "MT"},
    {"_NameGeo": "Netherlands", "_CodeGeo": "NL"},
    {"_NameGeo": "Austria", "_CodeGeo": "AT"},
    {"_NameGeo": "Portugal", "_CodeGeo": "PT"},
    {"_NameGeo": "Slovenia", "_CodeGeo": "SI"},
    {"_NameGeo": "Slovakia", "_CodeGeo": "SK"},
    {"_NameGeo": "Finland", "_CodeGeo": "FI"},
    {"_NameGeo": "Euro area – 20", "_CodeGeo": "EA20"},
    {"_NameGeo": "Euro area - 19 countries", "_CodeGeo": "EA19"},
]


records = []


for coicop in coicop_codes:
    for geo in geo_codes:
        vClassificationCOICOP = coicop["_ClassificationCOICOP"]
        vCodeIDCOICOP = coicop["_CodeIDCOICOP"]
        vCodeGeo = geo["_CodeGeo"]
        vNameGeo = geo["_NameGeo"]

        url = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr?format=JSON&geo={vCodeGeo}&coicop={vCodeIDCOICOP}&lang=en"
        """
            Host: https://ec.europa.eu/eurostat/api/dissemination
            Service: statistics
            Version: 1.0
            Response Type: data
            Dataset Code: prc_hicp_manr
            Formato: JSON
            Filter:
                - Geografía: ES, ....
                - Tiempo: Todos 
                - Coicop: CP00 ....
        """
        # print(f"Generada URL: {url}")

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()  # Convertir la respuesta a un diccionario de Python

            #print (data)
                        # Extraer los campos geo, time, y value
            
            time_series = data.get('value', {})

            # time_series_1 = data.get('dimension', {})
            time_series_1 = data.get('dimension', {}).get('time', {})
            # print("Contenido de 'time':", time_series_1)

            # Extraer el mapeo de índices a fechas
            try:
                index_to_date = {v: k for k, v in time_series_1['category']['index'].items()}
                # print("index_to_date generado exitosamente:", index_to_date)

            except KeyError:
                print("La clave 'time' no se encuentra en los datos.")

            for time, value in time_series.items():
                records.append({
                    "geo": vCodeGeo,
                    "time": time,
                    "value": value,
                    "index": index_to_date.get(int(time), time), 
                    "coicop": vClassificationCOICOP
                })
        else:
            print(f"Error al acceder a los datos: {response.status_code} para la URL: {url}")


# Crear un DataFrame con los campos geo, time, y value
df = pd.DataFrame(records)
carpeta = r"C:\DataAnalysis\Eurostat\datafilecsv"  # Ruta carpeta ficheros
nombre_archivo = os.path.join(carpeta, f"prc_hicp_manr_{fecha_actual}.csv")  # Crear el nombre del archivo con la fecha y configurar la ruta

print(f"Archivo guardado como: {nombre_archivo}")  # Mostrar nombre por consola
df.to_csv(nombre_archivo, index=False)  # Guardar los datos en CSV
