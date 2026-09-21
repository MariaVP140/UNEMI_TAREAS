# Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde
# en un diccionario contando repeticiones; (2) tenga método elemento_mas_frecuente() que
# retorne el elemento con mayor frecuencia; (3) tenga método frecuencia_elemento(elemento)
# que retorne cuántas veces aparece.

class ContadorFrecuencia:
    def __init__(self):
        self.elementos = {}

    def agregar_elemento(self,elemento):
        if elemento in self.elementos :
            self.elementos[elemento] += 1
        else:
            self.elementos [elemento]= 1

    def elemento_mas_frecuente(self):
        elemento_mayor = ""
        mayor = 0

        for elemento , frecuencia in self.elementos.items():
            if frecuencia > mayor :
                mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self,elemento):
        if elemento in self.elementos:
            return self.elementos[elemento]  # ingresa a la cantidad de frecuencia si el elemento se encuentra .

        return 0

contador1 = ContadorFrecuencia()
contador1.agregar_elemento("a")
contador1.agregar_elemento("b")
contador1.agregar_elemento("a")
contador1.agregar_elemento("a")

print(contador1.elementos)
print(contador1.elemento_mas_frecuente())
print(contador1.frecuencia_elemento("a"))

# Ejercicio de práctica: RegistroVotos

# Crea una clase RegistroVotos que:

# Tenga un método registrar_voto(opcion) que guarde en un diccionario cuántas veces ha sido seleccionada cada opción.
# Tenga un método opcion_mas_votada() que retorne la opción que tenga la mayor cantidad de votos.
# Tenga un método cantidad_votos(opcion) que retorne cuántos votos tiene una opción específica.
# Crea un objeto de la clase y utiliza sus métodos para comprobar que funcionan correctamente.

class RegistroVotos:
    def __init__(self):
        self.votos = {}

    def registrar_voto(self,opcion):
        if opcion in self.votos :
            self.votos[opcion] +=1
        else:
            self.votos[opcion] = 1

    def opcion_mas_votada(self):
        opcion_mayor = ""
        mayor = 0
        for opcion , votos in self.votos.items():
            if votos > mayor :
                mayor = votos 
                opcion_mayor = opcion
        return opcion_mayor

    def cantidad_votos(self,opcion):
        return self.votos.get(opcion,0)

res1=RegistroVotos()
res1.registrar_voto("lista A")
res1.registrar_voto("lista B")
res1.registrar_voto("lista A")
res1.registrar_voto("lista A")
res1.registrar_voto("lista B")

print(res1.votos)
print(res1.opcion_mas_votada())
print(res1.cantidad_votos("lista B"))

