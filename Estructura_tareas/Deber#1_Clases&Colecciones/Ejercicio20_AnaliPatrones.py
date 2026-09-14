# Clase AnalizadorPatrones que: (1) tenga método encontrar_palabras(texto, patron) que
# busque palabras que inicien con el patrón y retorne una lista; (2) tenga método
# agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; (3) tenga
# método palabras_unicas() usando un conjunto.

class AnalizadorPatrones():
    def __init__(self):
        self.textos = []

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        resultado = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self):
        palabras = set(self.textos)

        return palabras


ap = AnalizadorPatrones()

print(ap.encontrar_palabras("el gato está aquí", "g"))

print(ap.agrupar_por_longitud("el gato está aquí"))

print(ap.palabras_unicas())