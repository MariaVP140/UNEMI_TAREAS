# Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) que retorne una
# tupla con todos los divisores; (2) tenga método es_perfecto(numero) que retorne True si la
# suma de sus divisores (excepto él mismo) es igual a él; (3) tenga método
# encontrar_multiples_divisores(*numeros) que retorne un diccionario {número:
# tupla_divisores}.

class DivisorFinder():
    def __init__(self):
        self.numeros = {}

    def encontrar_divisores(self,num):
        divisores = ()

        for i in range(1,num+1):
            if num % i == 0:
                divisores = divisores + (i,)
            
        return divisores
    
    def es_perfecto(self,num):
        suma = 0

        for i in self.encontrar_divisores(num-1):
            suma = suma + i

        if suma == num :
            return True

    def encontrar_multiples_divisores(self,*numeros):
        for num in numeros:
                self.numeros[num]= self.encontrar_divisores(num)

        return self.numeros

divisor1=DivisorFinder()
print(divisor1.encontrar_divisores(12))
if divisor1.es_perfecto(5) :
    print(f"El numero 6 es perfecto")

print(divisor1.encontrar_multiples_divisores(5,6,3))

# Ejercicio de práctica — Números abundantes

# Crea una clase AnalizadorDivisores que:

# Tenga un método obtener_divisores(numero) que retorne una tupla con todos sus divisores.
# Tenga un método es_abundante(numero) que retorne True si la suma de sus divisores, excepto el mismo número, es mayor que él.
# Tenga un método analizar_numeros(*numeros) que retorne un diccionario {numero: True/False} indicando cuáles son abundantes.

class AnalizadorDivisores:
    def __init__(self):
        pass

    def obtener_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_abundante(self, numero):
        suma = 0

        for i in range(1, numero):
            if numero % i == 0:
                suma += i

        if suma > numero:
            return True
        return False

    def analizar_numeros(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.es_abundante(numero)

        return resultado


ad = AnalizadorDivisores()

print(ad.obtener_divisores(12))
print(ad.es_abundante(12))
print(ad.analizar_numeros(6, 10, 12))