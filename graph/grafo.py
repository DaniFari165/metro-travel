class Grafo:
    def __init__(self):
        self.adyacencias = {}

    def agregar_vertice(self, codigo):
        if codigo not in self.adyacencias:
            self.adyacencias[codigo] = []

    def agregar_arista(self, origen, destino, precio):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        self.adyacencias[origen].append((destino, precio))
        self.adyacencias[destino].append((origen, precio))

    def obtener_vecinos(self, codigo, criterio="costo"):
        vecinos_originales = self.adyacencias.get(codigo, [])

        if criterio == "costo":
            return vecinos_originales

        if criterio == "escalas":
            vecinos_con_peso_uno = []
            for vecino, _precio in vecinos_originales:
                vecinos_con_peso_uno.append((vecino, 1))
            return vecinos_con_peso_uno

        return vecinos_originales

    def obtener_vertices(self):
        return list(self.adyacencias.keys())

    def obtener_aristas_unicas(self):
        aristas = []
        vistas = set()

        for origen, vecinos in self.adyacencias.items():
            for destino, precio in vecinos:
                clave = tuple(sorted([origen, destino]))
                if clave not in vistas:
                    vistas.add(clave)
                    aristas.append((origen, destino, precio))

        return aristas

    def __str__(self):
        lineas = []
        for vertice, vecinos in self.adyacencias.items():
            lineas.append(f"{vertice} -> {vecinos}")
        return "\n".join(lineas)