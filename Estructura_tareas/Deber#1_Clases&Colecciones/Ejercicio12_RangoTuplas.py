# Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una
# tupla con números en ese rango; (2) tenga método elementos_en_multiples_rangos(*rangos)
# que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un
# conjunto.

class SelectorRango:
    def __init__(self):
        pass

    def crear_rango(self,inicio,fin):
        numeros = ()     # esta bien nada mas que seria  mas correcto hacer primero una lista , agregar los numeros en esa lista luego crear una tuple

        for num in range(inicio,fin+1):
            numeros = numeros + (num,)

        return numeros

    def elementos_en_multiples_rangos(self,*rangos):
        conjunto = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]
            
            for i in self.crear_rango(inicio,fin):
                conjunto.add(i)

        return list(conjunto)

selector1 = SelectorRango()

print(selector1.crear_rango(1,5))
print(selector1.elementos_en_multiples_rangos((1,3),(2,4),(5,8)))

# Ejercicio de práctica: AnalizadorNumeros

# Crea una clase AnalizadorNumeros que:

# Tenga un método registrar_grupo(*numeros) que guarde los números recibidos en una tupla.
# Tenga un método combinar_grupos(*grupos) que reciba varias tuplas de números y retorne una lista con todos los números sin repetir, utilizando un conjunto.
# Tenga un método repetidos_entre_grupos(grupo1, grupo2) que retorne una lista con los números que aparecen en ambos grupos, utilizando conjuntos.
# Crea un objeto de la clase y prueba los tres métodos.

class AnalizadorNumeros:
    def __init__(self):
        pass

    def registrar_grupo(self,*numeros):

        return numeros

    def combinar_grupos(self,*grupos):
        grup_sin_repetir = set()

        for grup in grupos:
            for g in grup:
                grup_sin_repetir.add(g)

        return list(grup_sin_repetir)

    def repetidos_entre_grupos(self, grupo1,grupo2):
        ambos_grupos =set()

        for grupo in grupo1:
            if grupo in grupo2:
                ambos_grupos.add(grupo)
                
        return list(ambos_grupos)


anali1= AnalizadorNumeros()

print(anali1.registrar_grupo(6,5,9,7))
print(anali1.combinar_grupos((6,5,9,7),(5,8,10,1)))
print(anali1.repetidos_entre_grupos((6,5,8),(6,8,9)))