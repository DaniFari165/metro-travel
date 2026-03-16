class Dijkstra:
    @staticmethod
    def calcular(grafo, origen, destino, criterio="costo", nodos_permitidos=None):
        """
        Retorna:
            (distancia_total, camino)
        Si no existe ruta:
            (None, [])
        """

        vertices = grafo.obtener_vertices()

        if origen not in vertices or destino not in vertices:
            return None, []

        if nodos_permitidos is not None:
            if origen not in nodos_permitidos or destino not in nodos_permitidos:
                return None, []

        distancias = {}
        anteriores = {}

        for vertice in vertices:
            distancias[vertice] = float("inf")
            anteriores[vertice] = None

        distancias[origen] = 0
        visitados = set()

        while len(visitados) < len(vertices):
            actual = Dijkstra._obtener_vertice_menor_distancia(
                distancias,
                visitados,
                nodos_permitidos
            )

            if actual is None:
                break

            if actual == destino:
                break

            visitados.add(actual)

            vecinos = grafo.obtener_vecinos(actual, criterio)

            for vecino, peso in vecinos:
                if vecino in visitados:
                    continue

                if nodos_permitidos is not None and vecino not in nodos_permitidos:
                    continue

                nueva_distancia = distancias[actual] + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual

        if distancias[destino] == float("inf"):
            return None, []

        camino = Dijkstra._reconstruir_camino(anteriores, origen, destino)

        if not camino:
            return None, []

        return distancias[destino], camino

    @staticmethod
    def _obtener_vertice_menor_distancia(distancias, visitados, nodos_permitidos=None):
        menor_vertice = None
        menor_distancia = float("inf")

        for vertice, distancia in distancias.items():
            if vertice in visitados:
                continue

            if nodos_permitidos is not None and vertice not in nodos_permitidos:
                continue

            if distancia < menor_distancia:
                menor_distancia = distancia
                menor_vertice = vertice

        return menor_vertice

    @staticmethod
    def _reconstruir_camino(anteriores, origen, destino):
        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()

        if len(camino) == 0 or camino[0] != origen:
            return []

        return camino