# Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; (2)
# tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]}
# reutilizando es_par; (3) tenga método cantidad_pares_impares() que retorne una tupla
# (cant_pares, cant_impares).

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self,num):

        if num % 2 == 0 :
            return True

        else :
            return False
    
    def separar (self,*numeros):

        for i in numeros:
            if self.es_par(i):
                self.pares.append(i)
            else :
                self.impares.append(i)

        return {
            "pares" : self.pares,
            "impares" : self.impares
        }

    def cantidad_pares_impares(self):
        return (len(self.pares)) , (len(self.impares))

numero1 = AnalizadorNumeros()

print(numero1.separar(1,2,3,4,5))
print(numero1.cantidad_pares_impares())

# Ejercicio de práctica: AnalizadorEdades

# Crea una clase AnalizadorEdades que:

# Tenga un método es_mayor_edad(edad) que retorne True si la edad es mayor o igual a 18, y False en caso contrario.
# Tenga un método clasificar(*edades) que reciba varias edades y retorne un diccionario:
# Reutilizando el método es_mayor_edad().
# Tenga un método cantidad_mayores_menores() que retorne una tupla:

# Crea un objeto de la clase y prueba los tres métodos.

class AnalizadorEdades:
    def __init__(self):
        self.mayores = []
        self.menores = []

    def es_mayor_edad(self,edad):
        if edad >= 18 :
            return True

        return False

    def clasificar (self,*edades):
        for edad in edades:
            if self.es_mayor_edad(edad):
                self.mayores.append(edad)
            else :
                self.menores.append(edad)
        
        return {
            "mayores" : self.mayores,
            "menores" : self.menores
        }

    def cantidad_mayores_menores(self):
        return len(self.mayores),len(self.menores)

analiza1=AnalizadorEdades()

print(analiza1.es_mayor_edad(16))
print(analiza1.clasificar(18,15,20,26))
print(analiza1.cantidad_mayores_menores())