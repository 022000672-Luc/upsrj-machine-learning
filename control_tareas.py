# Control automático de tareas académicas

    # Descripción del problema
#Como estudiante de Robótica Computacional, se manejan múltiples tareas, reportes y prácticas
#registradas en archivos Excel. Revisar manualmente las fechas de entrega para identificar
#tareas vencidas o próximas a vencer es una tarea repetitiva y propensa a errores.

    # Solución propuesta
#Se desarrolló un script en Python que lee un archivo Excel con las tareas académicas,
#analiza las fechas de entrega y clasifica automáticamente cada actividad según su estado:
#A tiempo, Por vencer o Atrasada. El sistema genera un nuevo archivo Excel con el reporte final.

    # Herramientas utilizadas
#- Python
#- Pandas
#- Excel


# control_tareas.py
import pandas as pd
from datetime import datetime

# Leer archivo CSV con codificación correcta (Excel típico en Windows)
df = pd.read_csv("tareas.csv", encoding="latin-1")

# Convertir columna de fechas a datetime (día primero)
df["fecha_entrega"] = pd.to_datetime(df["fecha_entrega"], dayfirst=True)

# Obtener fecha actual
hoy = datetime.now().date()

# Función para clasificar tareas según fecha de entrega
def clasificar(fecha):
    dias = (fecha.date() - hoy).days
    if dias < 0:
        return "Atrasada"
    elif dias <= 3:
        return "Por vencer"
    else:
        return "A tiempo"

# Aplicar la función a la columna fecha_entrega
df["estado"] = df["fecha_entrega"].apply(clasificar)

# Guardar el reporte final (CSV)
df.to_csv("reporte_tareas.csv", index=False, encoding="latin-1")

print("Reporte generado correctamente")
