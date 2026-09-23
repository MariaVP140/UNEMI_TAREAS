# Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤
# 100, False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, 
# las valide, agregue solo las válidas a una lista interna, y retorne esa lista; (3) tenga método 
# promedio() que retorne el promedio de notas almacenadas.

class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self,nota):
        valida = False
        if 0 <= nota <= 100 :
            valida = True

        return valida
    
    def cargar_notas(self,*args):
        lista_validada = []

        for num in args:
            if self.validar_nota(num):
                lista_validada.append(num)
                self.notas.append(num)

        return lista_validada

    def promedio(self):
        if len(self.notas) == 0:
             return 0
        return sum(self.notas) / len(self.notas)


calificacion1= Calificador()
print(calificacion1.validar_nota(80))
print(calificacion1.validar_nota(120))

print(calificacion1.cargar_notas(85,92,110,78,-5,88))
print(calificacion1.promedio())


# Ejercicio de práctica: ControlInventario

# Crear una clase ControlInventario que:

# Tenga un atributo productos que sea una lista vacía donde se almacenen las cantidades válidas de productos.
# Tenga un método validar_cantidad(cantidad) que retorne True si 0 ≤ cantidad ≤ 500, y False en caso contrario.
# Tenga un método cargar_cantidades(*args) que reciba múltiples cantidades, valide cada una y agregue solo las cantidades válidas a la lista productos. Debe retornar la lista.
# Tenga un método total_productos() que retorne la suma de todas las cantidades almacenadas en la lista.
# Crear un objeto de la clase y utilizar sus métodos para comprobar que el programa funciona correctamente.

class ControlInventario:
    def __init__(self):
        self.productos=[]

    def validar_cantidad(self,cantidad):
        if 0 <= cantidad <= 500 :
            return True
        return False

    def cargar_cantidades(self,*args):
        for i in args:
            if self.validar_cantidad(i):
                self.productos.append(i)

        return self.productos

    def total_productos(self):
        if len(self.productos) == 0:
            return 0
        return sum(self.productos)

control1= ControlInventario()

print(control1.validar_cantidad(100))
print(control1.cargar_cantidades(200,300,600))
print(control1.total_productos())