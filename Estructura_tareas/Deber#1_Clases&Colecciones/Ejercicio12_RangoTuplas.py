# Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una
# tupla con números en ese rango; (2) tenga método elementos_en_multiples_rangos(*rangos)
# que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un
# conjunto.

class SelectorRango():
    def __init__(self):
        pass

    def crear_rango(self,inicio,fin):
        numeros = ()

        for num in range(inicio,fin+1):
            numeros = numeros + (num,)

        return numeros

    def elementos_en_multiples_rangos(self,*rangos):
        conjunto = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]

            for i in range(inicio,fin + 1):
                conjunto.add(i)

        return list(conjunto)

selector1 = SelectorRango()

print(selector1.crear_rango(1,5))
print(selector1.elementos_en_multiples_rangos((1,3),(2,4),(5,8)))
