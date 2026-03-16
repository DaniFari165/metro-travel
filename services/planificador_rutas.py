from graph.dijkstra import Dijkstra


class PlanificadorRutas:
    def __init__(self, aeropuertos, grafo):
        self.aeropuertos = aeropuertos
        self.grafo = grafo

    def calcular_ruta(self, origen, destino, tiene_visa, criterio):
        origen = origen.strip().upper()
        destino = destino.strip().upper()

        if origen not in self.aeropuertos:
            return {
                "exito": False,
                "mensaje": f"El aeropuerto de origen '{origen}' no existe."
            }

        if destino not in self.aeropuertos:
            return {
                "exito": False,
                "mensaje": f"El aeropuerto de destino '{destino}' no existe."
            }

        if criterio not in ("costo", "escalas"):
            return {
                "exito": False,
                "mensaje": "Criterio inválido. Debe ser 'costo' o 'escalas'."
            }

        nodos_permitidos = self._obtener_nodos_permitidos(tiene_visa)

        if origen not in nodos_permitidos:
            return {
                "exito": False,
                "mensaje": f"No se puede iniciar en {origen} porque requiere visa y el pasajero no posee visa."
            }

        if destino not in nodos_permitidos:
            return {
                "exito": False,
                "mensaje": f"No se puede llegar a {destino} porque requiere visa y el pasajero no posee visa."
            }

        valor, ruta = Dijkstra.calcular(
            self.grafo,
            origen,
            destino,
            criterio=criterio,
            nodos_permitidos=nodos_permitidos
        )

        if not ruta:
            return {
                "exito": False,
                "mensaje": "No existe una ruta disponible con las restricciones indicadas."
            }

        resultado = {
            "exito": True,
            "ruta": ruta,
            "criterio": criterio
        }

        if criterio == "costo":
            resultado["costo_total"] = valor
            resultado["cantidad_vuelos"] = len(ruta) - 1
            resultado["escalas"] = max(0, len(ruta) - 2)
        else:
            resultado["cantidad_vuelos"] = valor
            resultado["escalas"] = max(0, len(ruta) - 2)
            resultado["costo_total"] = self._calcular_costo_real_de_ruta(ruta)

        return resultado

    def _obtener_nodos_permitidos(self, tiene_visa):
        permitidos = set()

        for codigo, aeropuerto in self.aeropuertos.items():
            if tiene_visa:
                permitidos.add(codigo)
            else:
                if not aeropuerto.requiere_visa:
                    permitidos.add(codigo)

        return permitidos

    def _calcular_costo_real_de_ruta(self, ruta):
        costo_total = 0

        for i in range(len(ruta) - 1):
            origen = ruta[i]
            destino = ruta[i + 1]

            vecinos = self.grafo.obtener_vecinos(origen, criterio="costo")

            for vecino, precio in vecinos:
                if vecino == destino:
                    costo_total += precio
                    break

        return costo_total