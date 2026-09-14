# Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) que guarde en
# un diccionario; (2) tenga método restar_stock(producto, cantidad) que disminuya y
# retorne True si hay suficiente; (3) tenga método productos_bajo_stock(minimo) que retorne
# una lista de productos con cantidad < minimo.

class Inventario():
    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] = self.productos[producto] + cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.productos:
            if self.productos[producto] >= cantidad:
                self.productos[producto] = self.productos[producto] - cantidad
                return True

        return False

    def productos_bajo_stock(self, minimo):
        bajo_stock = []

        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                bajo_stock.append(producto)

        return bajo_stock


inv = Inventario()

inv.agregar_stock("pan", 50)

print(inv.restar_stock("pan", 30))

print(inv.productos_bajo_stock(25))