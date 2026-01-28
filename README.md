# Control de Tareas Automatizado

## 1️ Descripción del proyecto
Este proyecto automatiza el seguimiento de tareas escolares para un estudiante de **Robótica Computacional**.  
Se clasifica automáticamente cada tarea según la fecha de entrega, generando un **reporte actualizado** con el estado de cada actividad.

---

## 2️ Problema que resuelve
Normalmente, los estudiantes revisamos nuestras tareas de manera manual en Excel o papel, lo que puede ser:

- Lento  
- Propenso a errores  
- Difícil de organizar  

Con este proyecto, **el proceso se automatiza** usando Python y un archivo CSV.

---

## 3️ Solución propuesta
Se desarrolló un **script en Python (`control_tareas.py`)** que:

1. Lee un archivo `tareas.csv` con la lista de tareas.  
2. Convierte las fechas de entrega a un formato que Python pueda interpretar.  
3. Calcula cuántos días faltan para la entrega.  
4. Crea una nueva columna llamada `estado` con valores:  
   - `Atrasada` → si la fecha ya pasó  
   - `Por vencer` → si faltan 0–3 días  
   - `A tiempo` → si falta más de 3 días  
5. Genera automáticamente un **reporte final** llamado `reporte_tareas.csv`.

---

## 4️ Archivos del proyecto

 Archivo, Descripción 

- `tareas.csv` - Archivo de entrada con todas las tareas (hecho en Excel o CSV). 
- `control_tareas.py` - Código Python que automatiza la clasificación de tareas. 
- `reporte_tareas.csv` - Archivo generado automáticamente con el estado de cada tarea. 
- `README.md` - Explicación del proyecto y cómo usarlo. 

---

## 5️ Instrucciones de uso

1. Coloca `tareas.csv` en la misma carpeta que `control_tareas.py`.  
2. Abre la terminal y activa tu entorno virtual:
```bash
source venv/bin/activate
