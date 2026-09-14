# Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en
# un diccionario; (2) tenga método personas_mayores(edad_minima) que retorne una lista de
# nombres cuya edad sea ≥; (3) tenga método edad_promedio() que retorne el promedio de
# edades.

class GestorPersonas():
    def __init__(self):
        self.persona = {}

    def agregar_persona(self,nombre,edad):
        self.persona[nombre] = edad

    def personas_mayores(self,edad_minima):
        mayores = []

        for nombre, edad in self.persona.items():
            if edad >= edad_minima:
                mayores.append(nombre)

            return mayores

    # def edad_promedio(self):
    #     prom = sum(self.persona.values())/ len(self.persona)

    #     return prom

    def edad_promedio(self):
        suma = 0

        for edad in self.persona.values():
            suma += edad

        return suma / len(self.persona)

persona1 = GestorPersonas()

persona1.agregar_persona("Ana",28)
persona1.agregar_persona("Bod",17)
print(persona1.personas_mayores(18))
print(persona1.edad_promedio())
print(persona1.persona)