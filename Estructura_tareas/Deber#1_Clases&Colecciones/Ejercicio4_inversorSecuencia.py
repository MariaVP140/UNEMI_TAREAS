# Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que 
# retorne la lista invertida sin usar reversed() (usa manual con bucles); (2) tenga método invertir_multiples(*listas) 
# que reutilice el anterior para invertir varias listas y retorne un diccionario {lista_original: lista_invertida}.

class InversorSecuencia():
    def __init__ (self):
        pass

    def invertir_lista(self,lista):
        lista_invertida = []
        for num in range(len(lista)-1,-1,-1):  # empieza en la longitud - 1 ya que empieza en 0 , baja hasta antes de -1 osea antes de ese valor el 1 , avanzando de -1 en -1.
            lista_invertida.append(lista[num])
            
        return(lista_invertida)

    def invertir_multiples(self,*listas):
        diccionario = {}
        for lis in listas :
            diccionario[tuple(lis)] = self.invertir_lista(lis)

            return diccionario
        

inversor1=InversorSecuencia()

print(inversor1.invertir_lista([1,2,3]))
resultado = inversor1.invertir_multiples([8,9,10],[5,6,7])
print(inversor1.invertir_multiples([8,9,10],[5,6,7]))

for original, invertida in resultado.items():
    print("Original:", original)
    print("Invertida:", invertida)