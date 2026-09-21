# 📋 Enunciado. Crear una clase NumeroPrimo que:
# Tenga un método es_primo(numero) que retorne True o False.
# Tenga un método primos_en_rango(*args) que reciba múltiples números y retorne una lista con los que son primos, reutilizando es_primo().
# Tenga un atributo historial (una lista) que guarde todos los números probados.
# Tenga un método cantidad_verificados() que retorne cuántos números se han probado.

class NumeroPrimo:
    def __init__(self):
        self.historial = []
        

    def es_primo(self,num):
        self.historial.append(num)
        primo = True

        if num < 2 :
            primo = False
        else : 
            for i in range(2,num):
                if num % i == 0 :
                    primo = False 
                    break

        return primo 

    def primos_en_rango(self, *args):
        primos = []

        for i in args :

            if self.es_primo(i):
                primos.append(i)


        return primos

    def cantidad_verificados (self):
        return len(self.historial)


primos1 = NumeroPrimo()
 
 
if primos1.es_primo(9):
    print("El numero es primo")
else:
    print(f"El numero 9 no es primo")

print(primos1.primos_en_rango(5,2,6))
print(primos1.historial)
print(primos1.cantidad_verificados())


# Ejercicio de práctica: AnalizadorDivisibles

# Crear una clase AnalizadorDivisibles que:

# Tenga un atributo historial que sea una lista y almacene todos los números analizados.
# Tenga un método es_divisible(numero, divisor) que reciba un número y un divisor, y retorne True si el número es divisible entre el divisor, o False en caso contrario. El número debe quedar registrado en historial.
# Tenga un método filtrar_divisibles(divisor, *args) que reciba un divisor y múltiples números, y retorne una lista con los números que sean divisibles entre dicho divisor. Debe reutilizar el método es_divisible().
# Tenga un método cantidad_analizados() que retorne la cantidad de números almacenados en historial.
# Crear un objeto de la clase y utilizar sus métodos para comprobar que el programa funciona correctamente.

class AnalizadorDivisibles:
    def __init__(self):
        self.historial=[]

    def es_divisible(self,numero,divisor):
        self.historial.append(numero)
        if numero % divisor == 0:
            return True
        return False
    
    def filtrar_divisibles(self,divisor,*args):
        divisores = []
        for i in args:
            if self.es_divisible(i,divisor):
                divisores.append(i)
        return divisores

    def cantidad_analizados(self):
        return len(self.historial)

Analizador1 = AnalizadorDivisibles()

print(Analizador1.es_divisible(5,2))
print(Analizador1.filtrar_divisibles(2,6,7,8,9,10))
print(Analizador1.cantidad_analizados())
print(Analizador1.historial)
