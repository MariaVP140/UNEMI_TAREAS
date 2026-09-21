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

# Ejercicio de práctica 19 — Control de materiales

# Crea una clase ControlMateriales que:

# Tenga un método agregar_material(material, cantidad) que almacene o aumente la cantidad en un diccionario.
# Tenga un método usar_material(material, cantidad) que disminuya la cantidad solamente cuando exista suficiente.
# Tenga un método materiales_escasos(limite) que retorne una lista con los materiales cuya cantidad sea menor al límite.

class ControlMateriales:
    def __init__(self):
        self.materiales = {}

    def agregar_material(self, material, cantidad):
        if material in self.materiales:
            self.materiales[material] += cantidad
        else:
            self.materiales[material] = cantidad

    def usar_material(self, material, cantidad):
        if material in self.materiales and self.materiales[material] >= cantidad:
            self.materiales[material] -= cantidad
            return True

        return False

    def materiales_escasos(self, limite):
        escasos = []

        for material, cantidad in self.materiales.items():
            if cantidad < limite:
                escasos.append(material)

        return escasos


cm = ControlMateriales()

cm.agregar_material("papel", 100)
cm.agregar_material("cartulina", 10)

print(cm.usar_material("papel", 30))
print(cm.usar_material("cartulina", 20))
print(cm.materiales_escasos(20))