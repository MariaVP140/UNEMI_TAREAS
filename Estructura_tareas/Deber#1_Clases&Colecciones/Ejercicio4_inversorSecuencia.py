# Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que 
# retorne la lista invertida sin usar reversed() (usa manual con bucles); (2) tenga método invertir_multiples(*listas) 
# que reutilice el anterior para invertir varias listas y retorne un diccionario {lista_original: lista_invertida}.

class InversorSecuencia:
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
print(inversor1.invertir_multiples([8,9,10],[5,6,7]))

# resultado = inversor1.invertir_multiples([8,9,10],[5,6,7])

# print(inversor1.invertir_multiples([8,9,10],[5,6,7]))

# for original, invertida in resultado.items():
#     print("Original:", original)
#     print("Invertida:", invertida)

# Ejercicio de práctica: SeparadorNumeros

# Crea una clase SeparadorNumeros que:

# Tenga un método separar_pares(lista) que reciba una lista de números y retorne una nueva lista únicamente con los números pares. No uses filter(); hazlo manualmente con un bucle.
# Tenga un método separar_multiples(*listas) que reciba varias listas, reutilice el método separar_pares() para cada una y retorne un diccionario con la lista original como clave y la lista de números pares como valor.
# Crea un objeto de la clase y prueba ambos métodos con varias listas.

class SeparadorNumeros:
    def __init__(self):
        pass

    def separar_pares(self,lista):
        lista_pares =[]
        
        for i in lista:
            if i % 2 == 0:
                lista_pares.append(i)

        return lista_pares

    def separar_multiples(self,*listas):
        diccionario = {}
        
        for lista in listas:
            diccionario[tuple(lista)] = self.separar_pares(lista)

        return diccionario


separador1=SeparadorNumeros()

print(separador1.separar_pares([5,8,10]))
print(separador1.separar_multiples([12,6,4],[16,3,9]))