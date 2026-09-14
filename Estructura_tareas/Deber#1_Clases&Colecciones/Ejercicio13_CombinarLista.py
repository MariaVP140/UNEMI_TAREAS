# Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne
# una lista alternando elementos de ambas; (2) tenga método intercalar_multiples(*listas)
# que reutilice para varias listas.

class CombinadorListas():
    def intercalar(self,lista1,lista2):
        elementos = []

        mayor = max(len(lista1),len(lista2))

        for i in range(mayor):
            if i < len(lista1):
                elementos.append(lista1[i])

            if i< len(lista2):
                elementos.append(lista2[i])

        return elementos

    def intercalar_multiples(self,*listas):
        resultado = []

        for lista in listas:
            resultado = self.intercalar(resultado,lista)  #"Toma lo que ya tengo en resultado y combínalo con la nueva lista usando el método intercalar."

        return resultado

combinador1= CombinadorListas()

print(combinador1.intercalar([1, 2], [3,4]))
print(combinador1.intercalar_multiples([1, 2], [3,4], [10, 20]))