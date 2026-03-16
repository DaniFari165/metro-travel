import math
import matplotlib.pyplot as plt


class VisualizadorRutas:
    @staticmethod
    def dibujar_grafo(grafo, ruta=None, titulo="Red de vuelos Metro Travel"):
        vertices = grafo.obtener_vertices()
        aristas = grafo.obtener_aristas_unicas()

        if not vertices:
            print("No hay vértices para graficar.")
            return

        posiciones = VisualizadorRutas._generar_posiciones_circulares(vertices)

        plt.figure(figsize=(12, 8))
        plt.title(titulo)

        # Dibujar todas las aristas
        for origen, destino, precio in aristas:
            x1, y1 = posiciones[origen]
            x2, y2 = posiciones[destino]

            plt.plot([x1, x2], [y1, y2], linewidth=1)

            xm = (x1 + x2) / 2
            ym = (y1 + y2) / 2
            plt.text(xm, ym, str(precio), fontsize=8)

        # Resaltar la ruta si existe
        if ruta and len(ruta) > 1:
            for i in range(len(ruta) - 1):
                origen = ruta[i]
                destino = ruta[i + 1]

                x1, y1 = posiciones[origen]
                x2, y2 = posiciones[destino]

                plt.plot([x1, x2], [y1, y2], linewidth=3)

        # Dibujar nodos
        for codigo, (x, y) in posiciones.items():
            plt.scatter(x, y, s=500)
            plt.text(x, y, codigo, ha="center", va="center", color="white", fontsize=9)

        plt.axis("off")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def _generar_posiciones_circulares(vertices):
        posiciones = {}
        cantidad = len(vertices)
        radio = 10

        for i, codigo in enumerate(vertices):
            angulo = 2 * math.pi * i / cantidad
            x = radio * math.cos(angulo)
            y = radio * math.sin(angulo)
            posiciones[codigo] = (x, y)

        return posiciones