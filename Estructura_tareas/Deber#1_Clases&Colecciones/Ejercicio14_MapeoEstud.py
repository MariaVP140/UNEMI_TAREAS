# Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un
# diccionario; (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de
# estudiantes; (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene
# mayor calificación.

class RegistroNotas():
    def __init__(self):
        self.estudiante={}

    def registrar(self,estudiante,nota):
        self.estudiante[estudiante]=nota
    
    def estudiantes_aprobados(self,nota_minima):
        aprobados = []

        for estudiantes,nota in self.estudiante.items():
            if nota >= nota_minima:
                aprobados.append(estudiantes)

        return estudiantes

    def mejor_estudiante(self):
        mejor = ""
        nota_mayor = 0

        for estudiantes,nota in self.estudiante.items():
            if nota > nota_mayor:
                nota_mayor = nota 
                mejor = estudiantes

        return mejor,nota_mayor

registro1= RegistroNotas()

registro1.registrar("Ana", 8)
registro1.registrar("Pedro", 6)
registro1.registrar("María", 9)
registro1.registrar("Luis", 7)

print(registro1.estudiante)
print(registro1.estudiantes_aprobados(70))
print(registro1.mejor_estudiante())