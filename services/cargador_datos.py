import csv
from models.aeropuerto import Aeropuerto
from models.vuelo import Vuelo


class CargadorDatos:
    @staticmethod
    def cargar_aeropuertos(ruta_archivo):
        aeropuertos = {}

        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                codigo = fila["codigo"]
                nombre = fila["nombre"]
                requiere_visa = fila["requiere_visa"].strip().lower() == "true"

                aeropuerto = Aeropuerto(codigo, nombre, requiere_visa)
                aeropuertos[aeropuerto.codigo] = aeropuerto

        return aeropuertos

    @staticmethod
    def cargar_vuelos(ruta_archivo):
        vuelos = []

        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                origen = fila["origen"]
                destino = fila["destino"]
                precio = float(fila["precio"])

                vuelos.append(Vuelo(origen, destino, precio))

        return vuelos