class Grafo:
    def __init__(self):
        # {
        #   "CCS": [("AUA", 40), ("CUR", 35)],
        #   "AUA": [("CCS", 40), ("CUR", 15)]
        # }
        self.adyacencias = {}

    def agregar_vertice(self, codigo):
        if codigo not in self.adyacencias:
            self.adyacencias[codigo] = []

    def agregar_arista(self, origen, destino, peso):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        self.adyacencias[origen].append((destino, peso))
        self.adyacencias[destino].append((origen, peso))  # bidireccional

    def obtener_vecinos(self, codigo):
        return self.adyacencias.get(codigo, [])

    def obtener_vertices(self):
        return list(self.adyacencias.keys())

    def __str__(self):
        texto = []
        for vertice, vecinos in self.adyacencias.items():
            texto.append(f"{vertice} -> {vecinos}")
        return "\n".join(texto)