# Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en
# un diccionario; (2) tenga método personas_mayores(edad_minima) que retorne una lista de
# nombres cuya edad sea ≥; (3) tenga método edad_promedio() que retorne el promedio de
# edades.

class GestorPersonas:
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
print(persona1.persona)
print(persona1.personas_mayores(18))
print(persona1.edad_promedio())


# Ejercicio de práctica: GestorProductos

# Crea una clase GestorProductos que:

# Tenga un método agregar_producto(nombre, precio) que guarde los productos y sus precios en un diccionario.
# Tenga un método productos_por_precio(precio_maximo) que retorne una lista con los nombres de los productos cuyo precio sea menor o igual al precio máximo indicado.
# Tenga un método precio_promedio() que retorne el promedio de los precios de todos los productos registrados.
# Crea un objeto y prueba los tres métodos con varios productos.

class GestorProductos:
    def __init__(self):
        self.productos={}

    def agregar_producto(self,nombre,precio):
        self.productos[nombre]=precio

    def productos_por_precio(self,precio_maximo):
        lista_max=[]
        for nombre,precio in self.productos.items():
            if precio <= precio_maximo:
                lista_max.append(nombre)

        return lista_max

    def precio_promedio(self):
        return sum(self.productos.values())/len(self.productos)

prod1=GestorProductos()

prod1.agregar_producto("arroz",1.50)
prod1.agregar_producto("CocaCola",3.00)
prod1.agregar_producto("helado de coco",0.50)
prod1.agregar_producto("Bambi",1.00)
print(prod1.productos)
print(prod1.productos_por_precio(1.00))
print(prod1.precio_promedio())