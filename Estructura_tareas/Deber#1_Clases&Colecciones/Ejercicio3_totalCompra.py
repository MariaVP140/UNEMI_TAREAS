# Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio)
# que guarde en un diccionario {nombre: precio}; (2) tenga método total_carrito() 
# que retorne la suma de todos los precios; (3) tenga método articulos_por_rango(precio_min, precio_max) 
# que retorne una lista con artículos dentro del rango.

class CarroCompras():
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