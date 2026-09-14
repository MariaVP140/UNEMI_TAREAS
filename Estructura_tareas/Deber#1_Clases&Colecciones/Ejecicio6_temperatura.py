# Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde
# en una lista; (2) tenga método minima()`, `maxima()`, `promedio() que calculen
# estadísticas; (3) tenga método registrar_multiples(*temps) que reutilice el registro para
# varias temperaturas.

class GestorTemperatura():
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

print(temperatura1.registrar_multiples(20,25,18,30))
print(temperatura1.promedio())
print(temperatura1.minima())
print(temperatura1.maxima())