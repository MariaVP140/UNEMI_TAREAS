# Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es
# vocal; (2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant,
# 'consonantes': cant, 'digitos': cant} reutilizando métodos; (3) tenga atributo que guarde el
# texto más largo analizado.

class AnalizadorString:
    def __init__(self):
        self.texto_largo = ""

    def solo_vocales(self, letras):
        vocal = {"a", "e", "i", "o", "u"}

        if letras.lower() in vocal:
            return True

        return False

    def solo_digitos(self, digito):

        if digito >= "0" and digito <= "9":
            return True

        return False

    def solo_consonates(self, cons):
        cons = cons.lower()

        if cons >= "a" and cons <= "z":
            if not self.solo_vocales(cons):
                return True

        return False

    def contar_por_tipo(self, texto):
        vocales = 0
        consonates = 0
        digitos = 0

        for i in texto:
            if self.solo_vocales(i):
                vocales += 1

            elif self.solo_digitos(i):
                digitos += 1

            elif self.solo_consonates(i):
                consonates += 1

        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto

        return {
            "vocales": vocales,
            "consonantes": consonates,
            "digitos": digitos
        }


tex1 = AnalizadorString()

print(tex1.contar_por_tipo("Hola como 123"))
print(tex1.texto_largo)

# Ejercicio de práctica: AnalizadorTexto

# Crea una clase AnalizadorTexto que:

# Tenga un método es_mayuscula(letra) que retorne True si la letra está en mayúscula y False en caso contrario.
# Tenga un método contar_por_tipo(texto) que retorne un diccionario:
# Debe reutilizar el método es_mayuscula().
# Tenga un atributo que guarde el texto más largo analizado.
# Crea un objeto de la clase y utiliza sus métodos para comprobar que funcionan correctamente.

class AnalizadorTexto:
    def __init__(self):
        self.texto= ""

    def es_mayuscula(self,letra):
        if letra >= "A" and letra <= "Z":
            return True
        return False

    def contar_por_tipo(self,texto):
        can_mayus = 0
        can_minus = 0
        can_dig = 0

        for i in texto :
            if self.es_mayuscula(i):
                can_mayus +=1
            elif i.isdigit():
                can_dig +=1
            elif i >= "a" and i <= "z":
                can_minus +=1
            
        if len(texto) > len(self.texto):
            self.texto = texto 

        return {
            "mayusculas" : can_mayus,
            "minusculas" : can_minus,
            "digitos" : can_dig
        }

texto1=AnalizadorTexto()

print(texto1.es_mayuscula("N"))
print(texto1.contar_por_tipo("La Gata es Mia12"))
print(texto1.texto)
print(texto1.contar_por_tipo("Las Rubias 12"))
print(texto1.texto)