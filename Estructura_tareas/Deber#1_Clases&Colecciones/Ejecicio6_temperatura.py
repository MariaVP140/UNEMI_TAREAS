# Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde
# en una lista; (2) tenga método minima()`, `maxima()`, `promedio() que calculen
# estadísticas; (3) tenga método registrar_multiples(*temps) que reutilice el registro para
# varias temperaturas.

class GestorTemperatura:
    def __init__(self):
        self.lista = []

    def registrar_temperatura(self,temp):
        self.lista.append(temp)

    def minima(self):
        return min(self.lista)

    def maxima (self):
        return max(self.lista)

    def promedio (self):
        return sum(self.lista)/len(self.lista)

    def registrar_multiples(self,*temps):
        for temp in temps :
            self.registrar_temperatura(temp)


temperatura1= GestorTemperatura()

temperatura1.registrar_multiples(20,25,18,30)
print(temperatura1.promedio())
print(temperatura1.minima())
print(temperatura1.maxima())

# Ejercicio de práctica: RegistroNotas

# Crea una clase RegistroNotas que:

# Tenga un método agregar_nota(nota) que guarde las notas en una lista.
# Tenga un método contar_aprobadas() que retorne cuántas notas son mayores o iguales a 70.
# Tenga un método nota_mayor() que retorne la nota más alta registrada.
# Tenga un método agregar_multiples(*notas) que reciba varias notas y reutilice agregar_nota() para almacenarlas.

class RegistroNotas:
    def __init__(self):
        self.notas=[]

    def agregar_nota(self,nota):
        self.notas.append(nota)

    def contar_aprobadas(self):
        contador = 0
        for nota in self.notas:
            if nota >= 70 :
                contador +=1
        
        return contador

    def nota_mayor(self):
        return max(self.notas)

    def agregar_multiples(self,*notas):
        for nota in notas :
            self.agregar_nota(nota)

registro1=RegistroNotas()

registro1.agregar_nota(80)
registro1.agregar_multiples(70,65,10,90,100)

print(registro1.notas)
print(registro1.contar_aprobadas())
print(registro1.nota_mayor())