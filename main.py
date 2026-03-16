from services.cargador_datos import CargadorDatos
from services.planificador_rutas import PlanificadorRutas
from services.visualizador_rutas import VisualizadorRutas
from graph.grafo import Grafo


def leer_codigo(mensaje):
    return input(mensaje).strip().upper()


def leer_visa():
    while True:
        respuesta = input("¿El pasajero tiene visa? (s/n): ").strip().lower()

        if respuesta in ("s", "si", "sí"):
            return True

        if respuesta in ("n", "no"):
            return False

        print("Entrada inválida. Escriba 's' o 'n'.")


def leer_criterio():
    while True:
        print("\nSeleccione criterio de optimización:")
        print("1. Menor costo")
        print("2. Menor cantidad de escalas")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            return "costo"

        if opcion == "2":
            return "escalas"

        print("Opción inválida. Intente nuevamente.")


def leer_desea_grafico():
    while True:
        respuesta = input("¿Desea ver la ruta gráficamente? (s/n): ").strip().lower()

        if respuesta in ("s", "si", "sí"):
            return True

        if respuesta in ("n", "no"):
            return False

        print("Entrada inválida. Escriba 's' o 'n'.")


def formatear_ruta_con_nombres(ruta, aeropuertos):
    partes = []
    for codigo in ruta:
        nombre = aeropuertos[codigo].nombre
        partes.append(f"{codigo} ({nombre})")
    return " -> ".join(partes)


def mostrar_resultado(resultado, aeropuertos):
    print("\n--- RESULTADO ---")

    if not resultado["exito"]:
        print(resultado["mensaje"])
        return

    print("Ruta encontrada:")
    print(formatear_ruta_con_nombres(resultado["ruta"], aeropuertos))

    if resultado["criterio"] == "costo":
        print(f"Costo total: {resultado['costo_total']}")
        print(f"Cantidad de vuelos: {resultado['cantidad_vuelos']}")
        print(f"Escalas: {resultado['escalas']}")
    else:
        print(f"Cantidad mínima de vuelos: {resultado['cantidad_vuelos']}")
        print(f"Escalas: {resultado['escalas']}")
        print(f"Costo real de esa ruta: {resultado['costo_total']}")


def main():
    aeropuertos = CargadorDatos.cargar_aeropuertos("data/aeropuertos.csv")
    vuelos = CargadorDatos.cargar_vuelos("data/vuelos.csv")

    grafo = Grafo()

    for codigo in aeropuertos:
        grafo.agregar_vertice(codigo)

    for vuelo in vuelos:
        grafo.agregar_arista(vuelo.origen, vuelo.destino, vuelo.precio)

    planificador = PlanificadorRutas(aeropuertos, grafo)

    print("===================================")
    print("   SISTEMA DE RUTAS METRO TRAVEL   ")
    print("===================================")

    while True:
        print("\nAeropuertos disponibles:")
        for aeropuerto in aeropuertos.values():
            print(aeropuerto)

        origen = leer_codigo("\nIngrese aeropuerto origen: ")
        destino = leer_codigo("Ingrese aeropuerto destino: ")
        tiene_visa = leer_visa()
        criterio = leer_criterio()

        resultado = planificador.calcular_ruta(origen, destino, tiene_visa, criterio)
        mostrar_resultado(resultado, aeropuertos)

        if resultado["exito"]:
            ver_grafico = leer_desea_grafico()
            if ver_grafico:
                VisualizadorRutas.dibujar_grafo(
                    grafo,
                    ruta=resultado["ruta"],
                    titulo=f"Ruta óptima: {origen} -> {destino}"
                )

        continuar = input("\n¿Desea consultar otra ruta? (s/n): ").strip().lower()
        if continuar not in ("s", "si", "sí"):
            print("Fin del programa.")
            break


if __name__ == "__main__":
    main()