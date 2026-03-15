from services.cargador_datos import CargadorDatos
from graph.grafo import Grafo

def main():
    aeropuertos = CargadorDatos.cargar_aeropuertos("data/aeropuertos.csv")
    vuelos = CargadorDatos.cargar_vuelos("data/vuelos.csv")

    grafo = Grafo()

    for codigo in aeropuertos:
        grafo.agregar_vertice(codigo)

    for vuelo in vuelos:
        grafo.agregar_arista(vuelo.origen, vuelo.destino, vuelo.precio)

    print("Aeropuertos cargados:")
    for aeropuerto in aeropuertos.values():
        print(aeropuerto)

    print("\nGrafo construido:")
    print(grafo)

if __name__ == "__main__":
    main()