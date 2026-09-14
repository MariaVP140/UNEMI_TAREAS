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
