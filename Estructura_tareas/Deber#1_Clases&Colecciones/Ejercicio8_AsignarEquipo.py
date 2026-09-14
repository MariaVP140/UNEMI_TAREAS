# Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo
# como una lista vacía en un diccionario; (2) tenga método agregar_jugador(equipo, jugador)
# que añada el jugador al equipo; (3) tenga método equipo_mayor_integrantes() que retorne el
# nombre del equipo con más jugadores.

# ------------------------------------------------------------------------------------
class Equipos():
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self,nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self,equipo,jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        equipo_mayor = ""
        mayor = 0

        for equipo , jugadores in self.equipos.items():
            if len(jugadores) > mayor :
                mayor =len(jugadores)
                equipo_mayor = equipo

        return equipo_mayor

equipo1 = Equipos()
equipo1.crear_equipo("A")
equipo1.agregar_jugador("A","juan")
equipo1.agregar_jugador("A","Pedro")
print(equipo1.equipo_mayor_integrantes())
print(equipo1.equipos)