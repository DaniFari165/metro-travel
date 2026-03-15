class Vuelo:
    def __init__(self, origen, destino, precio):
        self.origen = origen.strip().upper()
        self.destino = destino.strip().upper()
        self.precio = float(precio)

    def __str__(self):
        return f"{self.origen} <-> {self.destino} : ${self.precio:.2f}"