import os
import shutil
import pandas as pd

# Leer archivo CSV
datos = pd.read_csv("control_archivos.csv")

# Carpeta donde están los archivos
carpeta_base = "archivos_proyecto"

for _, fila in datos.iterrows():
    nombre_archivo = fila["archivo"]
    tipo = fila["tipo"]

    origen = os.path.join(carpeta_base, nombre_archivo)
    destino = os.path.join(carpeta_base, tipo)

    # Crear carpeta si no existe
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Mover archivo si existe
    if os.path.exists(origen):
        shutil.move(origen, destino)
        print(f"{nombre_archivo} movido a {tipo}")
    else:
        print(f"{nombre_archivo} no encontrado")
