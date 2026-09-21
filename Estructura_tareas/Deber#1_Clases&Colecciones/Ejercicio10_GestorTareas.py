# Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en
# una lista de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias() que
# retorne solo las de prioridad alta; (3) tenga método eliminar_completada(descripcion) que
# borre la tarea de la lista.

class Tareas:
    def __init__(self):
        self.tarea = []

    def agregar_tarea(self,descripcion,prioridad):
        self.tarea.append((descripcion,prioridad))

    def tareas_prioritarias(self):
        prioritarias = []

        for tarea in self.tarea:
            if tarea[1] == "alta":
                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self,descripcion):
        for tarea in self.tarea:
            if tarea[0] == descripcion:
                self.tarea.remove(tarea)
                break

tarea1 = Tareas()
tarea1.agregar_tarea("Estudiar","alta")
tarea1.agregar_tarea("Leer","baja")
tarea1.agregar_tarea("Nadar" , "alta")

print(tarea1.tarea)
print(tarea1.tareas_prioritarias())

tarea1.eliminar_completada("Estudiar")
print(tarea1.tarea)
print(tarea1.tareas_prioritarias())

# Ejercicio de práctica: RegistroCompras

# Crea una clase RegistroCompras que:

# Tenga un método agregar_compra(producto, categoria) que guarde cada compra en una lista de tuplas (producto, categoria).
# Tenga un método compras_alimentacion() que retorne únicamente las compras cuya categoría sea "alimentacion".
# Tenga un método eliminar_compra(producto) que elimine de la lista la compra cuyo producto coincida con el recibido.
# Crea un objeto de la clase y utiliza sus métodos para comprobar que funcionan correctamente.

class RegistroCompras:
    def __init__(self):
        self.compras=[]

    def agregar_compra(self,producto,categoria):
        self.compras.append((producto,categoria))

    def compras_alimentacion(self):
        alimentacion = []
        for compra in self.compras:
            if compra[1]=="alimento":
                alimentacion.append(compra)

        return alimentacion

    def eliminar_compra(self,producto):
        for compra in self.compras:
            if compra[0] == producto:
                self.compras.remove(compra)
                break

registro1=RegistroCompras()

registro1.agregar_compra("Armario","muebles")
registro1.agregar_compra("cocina","electrodomestico")
registro1.agregar_compra("pollo","alimento")
registro1.agregar_compra("arroz","alimento")

print(registro1.compras)
print(registro1.compras_alimentacion())

registro1.eliminar_compra("Armario")

print(registro1.compras)
