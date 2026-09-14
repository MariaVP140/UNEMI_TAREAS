# Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) que retorne la
# categoría ("niño", "adolescente", "adulto", "mayor"); (2) tenga método
# agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; (3
# tenga método edad_promedio_categoria(categoria).

class AgrupadorEdades():
    def __init__(self):
        self.edades = {}

    def clasificar_edad(self,edad):

        if edad >= 0 and edad <= 11:
            return "niño"
        elif edad >= 12 and edad <= 17:
            return "adolescente"
        elif edad >= 18 and edad <= 59:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self ,*edades):
        for edad in edades:
            categoria = self.clasificar_edad(edad)

            if categoria not in self.edades:
                self.edades[categoria] = []
                
                self.edades[categoria].append(edad)

        return self.edades

    def edad_promedio_categoria(self,categoria):
        suma = 0

        for edad in self.edades[categoria]:
            suma = suma + edad

        return suma / len(self.edades[categoria])

agrupar1= AgrupadorEdades()

print(agrupar1.clasificar_edad(15))

print(agrupar1.agrupar_por_categoria(5, 15, 30, 70))

print(agrupar1.edad_promedio_categoria("adulto"))

