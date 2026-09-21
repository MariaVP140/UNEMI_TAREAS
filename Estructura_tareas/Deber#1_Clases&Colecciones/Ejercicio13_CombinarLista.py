# Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne
# una lista alternando elementos de ambas; (2) tenga método intercalar_multiples(*listas)
# que reutilice para varias listas.

class CombinadorListas:
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

# Ejercicio de práctica: OrganizadorDeTurnos

# Crea una clase llamada OrganizadorDeTurnos que permita combinar participantes de diferentes turnos.

# combinar_turnos(turno1, turno2)
# Recibe dos listas.
# Debe crear y retornar una nueva lista colocando un elemento de turno1 y luego uno de turno2, alternadamente.
# Si una lista tiene más elementos que la otra, debe agregar los elementos que queden al final.
# combinar_varios_turnos(*turnos)
# Recibe varias listas.
# Debe utilizar el método combinar_turnos() para ir combinándolas.
# Debe retornar una sola lista con todos los elementos.
# Crea un objeto de la clase y realiza pruebas con diferentes listas para comprobar que los métodos funcionan correctamente.

class OrganizadorDeTurnos:
    def __init__(self):
        pass

    def combinar_turnos(self,turno1,turno2):
        turnos_alternados = []
        mayor = max(len(turno1),len(turno2))

        for i in range(mayor):
            if i < len(turno1):
                turnos_alternados.append(turno1[i])

            if i < len(turno2):
                turnos_alternados.append(turno2[i])

        return turnos_alternados

    def combinar_varios_turnos(self,*turnos):
        acumulador = []
        for turno in turnos:
            acumulador = self.combinar_turnos(acumulador,turno)
        
        return acumulador

orga1 = OrganizadorDeTurnos()
print(orga1.combinar_turnos(["11:00 am","14:00 pm","16:00 pm"],["13:00 am","15:00 pm"]))
print(orga1.combinar_varios_turnos(["10:00 am","12:00 pm","18:00 pm"],["11:00 am","13:00 pm",],["9:00 am","16:00 pm","17:00 pm","19:00"]))
