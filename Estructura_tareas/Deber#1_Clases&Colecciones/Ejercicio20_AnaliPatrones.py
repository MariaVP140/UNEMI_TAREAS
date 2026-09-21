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

# Ejercicio de práctica 20 — Analizador de palabras

# Crea una clase AnalizadorPalabras que:

# Tenga un método buscar_por_inicio(texto, inicio) que retorne las palabras que comiencen con determinado texto.
# Tenga un método organizar_por_tamano(texto) que agrupe las palabras en un diccionario según la cantidad de caracteres.
# Tenga un método obtener_sin_repetir() que retorne un conjunto con las palabras que hayan sido analizadas, eliminando las repetidas.

class AnalizadorPalabras:
    def __init__(self):
        self.texto = ""

    def buscar_por_inicio(self, texto, inicio):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(inicio):
                resultado.append(palabra)

        return resultado

    def organizar_por_tamano(self, texto):
        palabras = texto.split()
        grupos = {}

        for palabra in palabras:
            tamano = len(palabra)

            if tamano in grupos:
                grupos[tamano].append(palabra)
            else:
                grupos[tamano] = [palabra]

        self.texto = texto

        return grupos

    def obtener_sin_repetir(self):
        palabras = self.texto.split()

        return set(palabras)


aw = AnalizadorPalabras()

print(aw.buscar_por_inicio("casa camino perro carro", "ca"))
print(aw.organizar_por_tamano("sol luna casa perro"))
print(aw.obtener_sin_repetir())