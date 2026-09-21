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

# Ejercicio de práctica  — Transformador de letras

# Crea una clase TransformadorTexto que:

# Tenga un método desplazar_letra(letra, cantidad) que mueva una letra minúscula hacia adelante en el alfabeto utilizando %.
# Tenga un método transformar_texto(texto, cantidad) que reutilice desplazar_letra() para transformar todo el texto.
# Tenga un diccionario historial donde guarde el texto original como clave y el texto transformado como valor.

class TransformadorTexto:
    def __init__(self):
        self.historial = {}

    def desplazar_letra(self, letra, cantidad):
        codigo = ord(letra)
        nuevo_codigo = ((codigo - ord("a")) + cantidad) % 26
        return chr(nuevo_codigo + ord("a"))

    def transformar_texto(self, texto, cantidad):
        resultado = ""

        for letra in texto:
            resultado += self.desplazar_letra(letra, cantidad)

        self.historial[texto] = resultado

        return resultado


tt = TransformadorTexto()

print(tt.desplazar_letra("b", 4))
print(tt.transformar_texto("casa", 2))
print(tt.historial)