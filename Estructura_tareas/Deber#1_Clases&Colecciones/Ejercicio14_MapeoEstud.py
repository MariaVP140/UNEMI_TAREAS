# Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un
# diccionario; (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de
# estudiantes; (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene
# mayor calificación.

class RegistroNotas:
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

# Ejercicio de práctica: ControlCalificaciones

# Crea una clase llamada ControlCalificaciones que permita registrar las calificaciones de varios participantes.

# registrar_participante(nombre, calificacion)
# Debe guardar el nombre y la calificación en un diccionario.
# participantes_destacados(calificacion_minima)
# Debe retornar una lista con los nombres de los participantes cuya calificación sea mayor o igual al valor indicado.
# calificacion_mas_alta()
# Debe retornar el nombre del participante que tenga la calificación más alta junto con su calificación.
# Crea un objeto de la clase y realiza varias pruebas para comprobar que los tres métodos funcionan correctamente.

class ControlCalificaciones:
    def __init__(self):
        self.diccionario =  {}

    def registrar_participante(self,nombre,calificacion):
        self.diccionario[nombre] = calificacion

    def participantes_destacados(self,calificacion_minima):
        calificacion_mayor = []

        for nombre , calificacion in self.diccionario.items():
            if calificacion >= calificacion_minima:
                calificacion_mayor.append(nombre)

        return calificacion_mayor

    def calificacion_mas_alta(self):
        mayor = 0
        nombre_mayor = ""
        for nombre , calificacion in self.diccionario.items():
            if calificacion > mayor :
                mayor = calificacion
                nombre_mayor = nombre 

        return nombre_mayor,mayor


control1 = ControlCalificaciones()
control1.registrar_participante("Ana",90)
control1.registrar_participante("Jose",50)
control1.registrar_participante("Vanesa",70)

print(control1.diccionario)
print(control1.participantes_destacados(70))
print(control1.calificacion_mas_alta())