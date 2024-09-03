# Importar librerias
import requests
import pandas as pd
import os


###################################### Control de directorios

# Obtener la ruta absoluta del directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Verificar si la carpeta "datafilecsv" existe, si no, crearla
carpeta = os.path.join(script_dir, '..', 'datafilecsv')

if not os.path.exists(carpeta):
    os.makedirs(carpeta)

###################################### Control de tiempo

# Obtener datetime de ejecución
from datetime import datetime 
fecha_actual = datetime.now().strftime("%d-%m-%Y") #Formatear fecha DD/MM/YYYY

###################################### Funciones de obtención de datos

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

"""
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
"""

# Nuevo listado mas subfamilias
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
    {"_ClassificationCOICOP": "Food", "_CodeIDCOICOP": "CP011"},
    {"_ClassificationCOICOP": "Bread and cereals", "_CodeIDCOICOP": "CP0111"},
    {"_ClassificationCOICOP": "Rice", "_CodeIDCOICOP": "CP01111"},
    {"_ClassificationCOICOP": "Flours and other cereals", "_CodeIDCOICOP": "CP01112"},
    {"_ClassificationCOICOP": "Bread", "_CodeIDCOICOP": "CP01113"},
    {"_ClassificationCOICOP": "Other bakery products", "_CodeIDCOICOP": "CP01114"},
    {"_ClassificationCOICOP": "Pizza and quiche", "_CodeIDCOICOP": "CP01115"},
    {"_ClassificationCOICOP": "Pasta products and couscous", "_CodeIDCOICOP": "CP01116"},
    {"_ClassificationCOICOP": "Breakfast cereals", "_CodeIDCOICOP": "CP01117"},
    {"_ClassificationCOICOP": "Other cereal products", "_CodeIDCOICOP": "CP01118"},
    {"_ClassificationCOICOP": "Meat", "_CodeIDCOICOP": "CP0112"},
    {"_ClassificationCOICOP": "Beef and veal", "_CodeIDCOICOP": "CP01121"},
    {"_ClassificationCOICOP": "Pork", "_CodeIDCOICOP": "CP01122"},
    {"_ClassificationCOICOP": "Lamb and goat", "_CodeIDCOICOP": "CP01123"},
    {"_ClassificationCOICOP": "Poultry", "_CodeIDCOICOP": "CP01124"},
    {"_ClassificationCOICOP": "Other meats", "_CodeIDCOICOP": "CP01125"},
    {"_ClassificationCOICOP": "Edible offal", "_CodeIDCOICOP": "CP01126"},
    {"_ClassificationCOICOP": "Dried, salted or smoked meat", "_CodeIDCOICOP": "CP01127"},
    {"_ClassificationCOICOP": "Other meat preparations", "_CodeIDCOICOP": "CP01128"},
    {"_ClassificationCOICOP": "Fish and seafood", "_CodeIDCOICOP": "CP0113"},
    {"_ClassificationCOICOP": "Fresh or chilled fish", "_CodeIDCOICOP": "CP01131"},
    {"_ClassificationCOICOP": "Frozen fish", "_CodeIDCOICOP": "CP01132"},
    {"_ClassificationCOICOP": "Fresh or chilled seafood", "_CodeIDCOICOP": "CP01133"},
    {"_ClassificationCOICOP": "Frozen seafood", "_CodeIDCOICOP": "CP01134"},
    {"_ClassificationCOICOP": "Dried, smoked or salted fish and seafood", "_CodeIDCOICOP": "CP01135"},
    {"_ClassificationCOICOP": "Other preserved or processed fish and seafood and fish and seafood preparations", "_CodeIDCOICOP": "CP01136"},
    {"_ClassificationCOICOP": "Milk, cheese and eggs", "_CodeIDCOICOP": "CP0114"},
    {"_ClassificationCOICOP": "Fresh whole milk", "_CodeIDCOICOP": "CP01141"},
    {"_ClassificationCOICOP": "Fresh low fat milk", "_CodeIDCOICOP": "CP01142"},
    {"_ClassificationCOICOP": "Preserved milk", "_CodeIDCOICOP": "CP01143"},
    {"_ClassificationCOICOP": "Yoghurt", "_CodeIDCOICOP": "CP01144"},
    {"_ClassificationCOICOP": "Cheese and curd", "_CodeIDCOICOP": "CP01145"},
    {"_ClassificationCOICOP": "Other milk products", "_CodeIDCOICOP": "CP01146"},
    {"_ClassificationCOICOP": "Eggs", "_CodeIDCOICOP": "CP01147"},
    {"_ClassificationCOICOP": "Oils and fats", "_CodeIDCOICOP": "CP0115"},
    {"_ClassificationCOICOP": "Butter", "_CodeIDCOICOP": "CP01151"},
    {"_ClassificationCOICOP": "Margarine and other vegetable fats", "_CodeIDCOICOP": "CP01152"},
    {"_ClassificationCOICOP": "Olive oil", "_CodeIDCOICOP": "CP01153"},
    {"_ClassificationCOICOP": "Other edible oils", "_CodeIDCOICOP": "CP01154"},
    {"_ClassificationCOICOP": "Other edible animal fats", "_CodeIDCOICOP": "CP01155"},
    {"_ClassificationCOICOP": "Fruit", "_CodeIDCOICOP": "CP0116"},
    {"_ClassificationCOICOP": "Fresh or chilled fruit", "_CodeIDCOICOP": "CP01161"},
    {"_ClassificationCOICOP": "Frozen fruit", "_CodeIDCOICOP": "CP01162"},
    {"_ClassificationCOICOP": "Dried fruit and nuts", "_CodeIDCOICOP": "CP01163"},
    {"_ClassificationCOICOP": "Preserved fruit and fruit-based products", "_CodeIDCOICOP": "CP01164"},
    {"_ClassificationCOICOP": "Vegetables", "_CodeIDCOICOP": "CP0117"},
    {"_ClassificationCOICOP": "Fresh or chilled vegetables other than potatoes and other tubers", "_CodeIDCOICOP": "CP01171"},
    {"_ClassificationCOICOP": "Frozen vegetables other than potatoes and other tubers", "_CodeIDCOICOP": "CP01172"},
    {"_ClassificationCOICOP": "Dried vegetables, other preserved or processed vegetables", "_CodeIDCOICOP": "CP01173"},
    {"_ClassificationCOICOP": "Potatoes", "_CodeIDCOICOP": "CP01174"},
    {"_ClassificationCOICOP": "Crisps", "_CodeIDCOICOP": "CP01175"},
    {"_ClassificationCOICOP": "Other tubers and products of tuber vegetables", "_CodeIDCOICOP": "CP01176"},
    {"_ClassificationCOICOP": "Sugar, jam, honey, chocolate and confectionery", "_CodeIDCOICOP": "CP0118"},
    {"_ClassificationCOICOP": "Sugar", "_CodeIDCOICOP": "CP01181"},
    {"_ClassificationCOICOP": "Jams, marmalades and honey", "_CodeIDCOICOP": "CP01182"},
    {"_ClassificationCOICOP": "Chocolate", "_CodeIDCOICOP": "CP01183"},
    {"_ClassificationCOICOP": "Confectionery products", "_CodeIDCOICOP": "CP01184"},
    {"_ClassificationCOICOP": "Edible ices and ice cream", "_CodeIDCOICOP": "CP01185"},
    {"_ClassificationCOICOP": "Artificial sugar substitutes", "_CodeIDCOICOP": "CP01186"},
    {"_ClassificationCOICOP": "Food products n.e.c.", "_CodeIDCOICOP": "CP0119"},
    {"_ClassificationCOICOP": "Sauces, condiments", "_CodeIDCOICOP": "CP01191"},
    {"_ClassificationCOICOP": "Salt, spices and culinary herbs", "_CodeIDCOICOP": "CP01192"},
    {"_ClassificationCOICOP": "Baby food", "_CodeIDCOICOP": "CP01193"},
    {"_ClassificationCOICOP": "Ready-made meals", "_CodeIDCOICOP": "CP01194"},
    {"_ClassificationCOICOP": "Other food products n.e.c.", "_CodeIDCOICOP": "CP01199"},
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

def extract_data():
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
    # carpeta = r"C:\DataAnalysis\Eurostat\datafilecsv"  # Ruta carpeta ficheros
    tmpnombre = f"prc_hicp_manr_{fecha_actual}.csv"
    nombre_archivo = os.path.join(carpeta, f"{tmpnombre}")  # Crear el nombre del archivo con la fecha y configurar la ruta

    print(f"Archivo guardado como: {nombre_archivo}")  # Mostrar nombre por consola
    df.to_csv(nombre_archivo, index=False)  # Guardar los datos en CSV

    # Después de guardar el CSV, guardamos el nombre del archivo en un archivo de texto
    with open(os.path.join(carpeta, "latest_output.txt"), "w") as f:
        f.write(nombre_archivo)
    
    print(f"Nombre del archivo CSV guardado:{nombre_archivo}")
    print(f"Nombre del archivo TXT actualizado: latest_output.txt")

    return tmpnombre


if __name__ == "__main__":
    # Ejecutar la función de extracción
    generated_csv = extract_data()
    print(f"Archivo CSV generado: {generated_csv}")


