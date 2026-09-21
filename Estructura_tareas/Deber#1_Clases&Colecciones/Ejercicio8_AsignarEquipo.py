# Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo
# como una lista vacía en un diccionario; (2) tenga método agregar_jugador(equipo, jugador)
# que añada el jugador al equipo; (3) tenga método equipo_mayor_integrantes() que retorne el
# nombre del equipo con más jugadores.

class Equipos:
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
equipo1.crear_equipo("B")

equipo1.agregar_jugador("A","juan")
equipo1.agregar_jugador("A","Pedro")
equipo1.agregar_jugador("B","Sofia")
equipo1.agregar_jugador("B","Luisa")
equipo1.agregar_jugador("B","Juana")

print(equipo1.equipo_mayor_integrantes())
print(equipo1.equipos)

# Ejercicio de práctica: OrganizadorCursos

# Crea una clase OrganizadorCursos que:

# Tenga un método crear_curso(nombre_curso) que cree un curso como una lista vacía dentro de un diccionario.
# Tenga un método agregar_estudiante(curso, estudiante) que añada el estudiante a la lista del curso indicado.
# Tenga un método curso_mayor_estudiantes() que retorne el nombre del curso que tenga más estudiantes.
# Crea un objeto de la clase y utiliza sus métodos para comprobar que funcionan correctamente.

class OrganizadorCursos:
    def __init__(self):
        self.cursos={}

    def crear_curso(self,nombre_curso):
        self.cursos[nombre_curso]= []

    def agregar_estudiante(self,curso,estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor_estudiantes(self):
        mayor_estudiantes = ""
        mayor = 0

        for curso , estudiante in self.cursos.items():
            if len(estudiante) > mayor :
                mayor = len(estudiante)
                mayor_estudiantes = curso

        return mayor_estudiantes

organizar1= OrganizadorCursos()

organizar1.crear_curso("B1")
organizar1.crear_curso("B2")

organizar1.agregar_estudiante("B1","Arelys")
organizar1.agregar_estudiante("B1","Maria")
organizar1.agregar_estudiante("B1","Romina")
organizar1.agregar_estudiante("B2","Carlos")
organizar1.agregar_estudiante("B2","Diego")
print(organizar1.cursos)
print(organizar1.curso_mayor_estudiantes())