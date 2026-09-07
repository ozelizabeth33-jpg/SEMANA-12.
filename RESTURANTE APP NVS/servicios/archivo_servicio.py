import json
import os


class ArchivoServicio:
    def __init__(self, carpeta_datos="datos"):
        self.carpeta_datos = carpeta_datos

    def guardar(self, nombre_archivo, datos):
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def cargar(self, nombre_archivo):
        ruta = os.path.join(self.carpeta_datos, nombre_archivo)

        if not os.path.exists(ruta):
            return []

        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)