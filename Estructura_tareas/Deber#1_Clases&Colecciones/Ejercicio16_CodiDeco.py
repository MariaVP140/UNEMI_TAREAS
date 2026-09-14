# Clase CodificadorCesar que: (1) tenga método codificar_letra(letra, desplazamiento)
# que retorne la letra desplazada en el alfabeto (usar operador %); (2) tenga método
# codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; (3) tenga un
# diccionario como atributo para historial de codificaciones.

class CodificadorCesar():
    def __init__(self):
        self.historial_codificaciones = {}

    def codificar_letra(self,letra,desplazamiento):
        posicion = ord(letra.lower()) - ord("a")
        nueva_posicion = (posicion + desplazamiento) % 26
        nueva_letra = chr(nueva_posicion + ord("a"))

        return nueva_letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado = resultado + self.codificar_letra(letra, desplazamiento)

        self.historial_codificaciones[palabra] = resultado

        return resultado


codificador1 = CodificadorCesar()
print(codificador1.codificar_palabra("Hola",3))
print(codificador1.codificar_letra("l",2))
print(codificador1.historial_codificaciones)