# Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde
# en un diccionario contando repeticiones; (2) tenga método elemento_mas_frecuente() que
# retorne el elemento con mayor frecuencia; (3) tenga método frecuencia_elemento(elemento)
# que retorne cuántas veces aparece.

class ContadorFrecuencia():
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