# Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio)
# que guarde en un diccionario {nombre: precio}; (2) tenga método total_carrito() 
# que retorne la suma de todos los precios; (3) tenga método articulos_por_rango(precio_min, precio_max) 
# que retorne una lista con artículos dentro del rango.

class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self,nombre,precio):
        self.articulos[nombre] = precio # Python está guardando el nombre como clave y el precio como valor dentro del diccionario.

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self,precio_min,precio_max):
        lista = []
        for nombre,precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                lista.append((nombre,precio))

        return lista

carro1 = CarroCompras()
carro1.agregar_articulo("pan",2.50)
carro1.agregar_articulo("leche",3.00)
print(carro1.total_carrito())
print(carro1.articulos_por_rango(1,4))

# Ejercicio de práctica: CatalogoPeliculas

# Crear una clase CatalogoPeliculas que:

# Tenga un atributo peliculas que sea un diccionario donde se almacene {titulo: duracion}.
# Tenga un método agregar_pelicula(titulo, duracion) que agregue una película al diccionario utilizando el título como clave y la duración como valor.
# Tenga un método duracion_total() que retorne la suma de las duraciones de todas las películas almacenadas.
# Tenga un método peliculas_por_duracion(duracion_min, duracion_max) que retorne una lista con los títulos de las películas cuya duración se encuentre dentro del rango indicado.
# Crear un objeto de la clase y utilizar sus métodos para comprobar que el programa funciona correctamente.

class CatalogoPeliculas:
    def __init__(self):
        self.peliculas = {}

    def agregar_peliculas(self,titulo,duracion):
        self.peliculas[titulo]=duracion
    
    def duracion_total(self):
        return sum(self.peliculas.values())

    def peliculas_por_duracion(self,duracion_min,duracion_max):
        lista_rango=[]
        for titulo,duracion in self.peliculas.items():
            if duracion_min <= duracion <= duracion_max:
                lista_rango.append(titulo)

        return lista_rango

catalogo1 = CatalogoPeliculas()

catalogo1.agregar_peliculas("Dumbo",64)
catalogo1.agregar_peliculas("La sirenita",83)
catalogo1.agregar_peliculas("La Bella y la Bestia",84)
catalogo1.agregar_peliculas("El rey león",88)
catalogo1.agregar_peliculas("Frozen",102)

print(catalogo1.peliculas)
print(catalogo1.duracion_total())

print(catalogo1.peliculas_por_duracion(80,90))
