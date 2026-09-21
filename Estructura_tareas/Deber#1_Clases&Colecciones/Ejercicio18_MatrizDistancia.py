# Clase CalculadorDistancia que: (1) tenga método distancia_euclidiana(p1, p2) que
# reciba dos tuplas (x,y) y calcule la distancia; (2) tenga método
# punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; (3)
# tenga un atributo lista para guardar todas las distancias calculadas.

class CalculadorDistancia():
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = puntos[0]
        distancia_menor = self.distancia_euclidiana(referencia, puntos[0])

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano


cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))
                   # punto referencia
print(cd.punto_mas_cercano((0, 0), (3, 4), (1, 2), (5, 5)))

print(cd.distancias)

# Ejercicio de práctica 18 — Comparador de puntos

# Crea una clase AnalizadorPuntos que:

# Tenga un método calcular_distancia(punto1, punto2) para calcular la distancia entre dos puntos.
# Tenga un método punto_mas_lejano(referencia, *puntos) que encuentre el punto más alejado de una referencia.
# Tenga una lista como atributo para guardar las distancias calculadas.

import math

class AnalizadorPuntos:
    def __init__(self):
        self.distancias = []

    def calcular_distancia(self, punto1, punto2):
        x1 = punto1[0]
        y1 = punto1[1]

        x2 = punto2[0]
        y2 = punto2[1]

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_lejano(self, referencia, *puntos):
        punto_lejano = None
        mayor = 0

        for punto in puntos:
            distancia = self.calcular_distancia(referencia, punto)

            if distancia > mayor:
                mayor = distancia
                punto_lejano = punto

        return punto_lejano


ap = AnalizadorPuntos()

print(ap.calcular_distancia((0, 0), (3, 4)))
print(ap.punto_mas_lejano((0, 0), (1, 1), (3, 4), (2, 2)))
print(ap.distancias)