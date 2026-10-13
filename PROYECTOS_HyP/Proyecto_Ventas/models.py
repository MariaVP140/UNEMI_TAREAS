from datetime import date


# =====================================================================
# CLASE BASE: lo que los tres modelos comparten
# =====================================================================
class ModeloBase:
    """Padre de todos los modelos. Guarda el id y define el comportamiento común."""

    def __init__(self, id_registro):
        self.id = int(id_registro)

    # ---- ÚNICO MÉTODO DE CLASE DEL PROYECTO ----
    @classmethod
    def desde_diccionario(cls, datos):
        """Diccionario -> objeto. Escrito UNA vez y usado por los tres modelos.
        cls es la clase que llamó: Cliente, Producto o Venta."""
        datos = dict(datos)                 # copia, para no tocar el original
        id_registro = datos.pop("id")       # saco el id
        return cls(id_registro, **datos)    # el resto son los campos del modelo

    # ---- MÉTODOS DE INSTANCIA ----
    def a_diccionario(self):
        # Objeto -> diccionario. Cada hijo agrega sus campos.
        return {"id": self.id}

    def etiqueta(self):
        # POLIMORFISMO: cada hijo la reescribe a su manera
        return f"registro {self.id}"

    def __str__(self): # es un método especial que permite decidir qué texto se mostrará cuando imprimimos un objeto con print().
        # Lo que se ve al hacer print(objeto). Llama a etiqueta(),
        # así que cada modelo se imprime distinto sin cambiar esta línea.
        return f"[{self.id}] {self.etiqueta()}"


# =====================================================================
# HERENCIA: Persona es la base de Cliente (y mañana, de Estudiante)
# =====================================================================
class Persona(ModeloBase):
    """Todo lo que tiene una persona del sistema."""

    def __init__(self, id_registro, nombre, apellido, email):  
        super().__init__(id_registro)      # el padre guarda el id ,super() permite acceder a métodos de la clase padre.
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        datos = super().a_diccionario()    # {"id": ...} que arma el padre
        datos["nombre"] = self.nombre
        datos["apellido"] = self.apellido
        datos["email"] = self.email
        return datos

    def etiqueta(self):
        return self.nombre_completo()


class Cliente(Persona):
    """Cliente ES UNA Persona, con teléfono y ciudad."""

    def __init__(self, id_registro, nombre, apellido, email, telefono="", ciudad=""):
        super().__init__(id_registro, nombre, apellido, email)
        self.telefono = telefono
        self.ciudad = ciudad

    def a_diccionario(self):
        datos = super().a_diccionario()    # reutiliza lo de Persona
        datos["telefono"] = self.telefono
        datos["ciudad"] = self.ciudad
        return datos

    def etiqueta(self):
        # Sobrescribe y EXTIENDE la del padre
        return f"{super().etiqueta()} · {self.email} · {self.ciudad or 'sin ciudad'}"


if __name__ == "__main__":
    cliente = Cliente(1, "Ana", "Pérez", "ana@example.com", ciudad="Guayaquil")
    print(cliente.a_diccionario())
    print("El objeto", cliente.desde_diccionario({'id': 1, 'nombre': 'Ana', 'apellido': 'Pérez', 'email': 'ana@example.com', 'telefono': '', 'ciudad': 'Guayaquil'}))
    print("Nombre completo heredado de Persona:", cliente.nombre_completo())




# =====================================================================
# ÚNICA CLASE CON ATRIBUTOS Y MÉTODOS ESTÁTICOS
# =====================================================================
class Producto(ModeloBase):
    """Producto ES UN ModeloBase. Aquí viven los ejemplos de lo estático."""

    # ATRIBUTOS ESTÁTICOS (de clase): existen una sola vez, no por objeto
    STOCK_MINIMO = 5          # regla del negocio, igual para todos los productos
    IVA = 0.15                # 15 %
    total_creados = 0         # contador compartido

    def __init__(self, id_registro, nombre, precio, stock=0):
        super().__init__(id_registro)
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)
        Producto.total_creados += 1        # se modifica en la CLASE, no en self

    # MÉTODOS ESTÁTICOS: reglas que no necesitan ningún producto concreto
    @staticmethod  #Indica que el método es estático. En este caso, no necesita acceder a los datos de un producto específico mediante self.
    def es_precio_valido(valor):
        try:
            return float(valor) > 0
        except (TypeError, ValueError):
            return False

    @staticmethod
    def con_iva(monto):
        return round(monto * (1 + Producto.IVA), 2)

    # MÉTODOS DE INSTANCIA: necesitan los datos de ESTE producto
    def stock_bajo(self):
        return self.stock <= Producto.STOCK_MINIMO

    def hay_stock(self, cantidad):
        return 0 < cantidad <= self.stock

    def descontar_stock(self, cantidad):
        self.stock -= cantidad

    def devolver_stock(self, cantidad):
        self.stock += cantidad

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["nombre"] = self.nombre
        datos["precio"] = self.precio
        datos["stock"] = self.stock
        return datos

    def etiqueta(self):
        alerta = " ⚠ stock bajo" if self.stock_bajo() else ""
        return f"{self.nombre} · ${self.precio:.2f} · stock {self.stock}{alerta}"


# =====================================================================
class Venta(ModeloBase):
    """Venta simple: un cliente, un producto, una cantidad."""

    def __init__(self, id_registro, cliente_id, producto_id, cantidad,
                 precio_unitario, fecha=""):
        super().__init__(id_registro)
        self.cliente_id = int(cliente_id)
        self.producto_id = int(producto_id)
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)
        self.fecha = fecha or date.today().isoformat()

    def calcular_total(self):
        # Se calcula cada vez; NO se guarda como atributo para que nunca
        # quede desactualizado si cambia la cantidad
        return round(self.cantidad * self.precio_unitario, 2)

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["cliente_id"] = self.cliente_id
        datos["producto_id"] = self.producto_id
        datos["cantidad"] = self.cantidad
        datos["precio_unitario"] = self.precio_unitario
        datos["fecha"] = self.fecha
        return datos

    def etiqueta(self):
        return (f"{self.fecha} · cliente {self.cliente_id} · "
                f" producto {self.producto_id} . {self.cantidad} x {self.precio_unitario} "
                f"= ${self.calcular_total():.2f}")


if __name__ == "__main__":

    # 1) ModeloBase: la clase padre. Solo guarda un id.
    #    Normalmente no se usa sola, pero se puede instanciar.
    base = ModeloBase(1)
    print(base)                        # [1] registro 1

    # 2) Persona: hereda de ModeloBase y agrega nombre, apellido y email.
    persona = Persona(2, "Ana", "Pérez", "ana@mail.com")
    print(persona)                     # [2] Ana Pérez

    # 3) Cliente: hereda de Persona (que a su vez hereda de ModeloBase).
    #    Por eso tiene id + nombre + apellido + email + teléfono + ciudad.
    cliente = Cliente(3, "Luis", "Mora", "luis@mail.com", "0991234567", "Milagro")
    print(cliente)                     # mismo print, pero se ve distinto: POLIMORFISMO
    print(cliente.a_diccionario())     # objeto -> diccionario (listo para guardar)

    # 4) Producto: usa atributos y métodos ESTÁTICOS (de la clase, no del objeto).
    print(Producto.es_precio_valido(-5))   # False -> se llama sin crear ningún producto
    producto = Producto(10, "Mouse", 20, stock=30)
    print(producto)                        # [10] Mouse · $20.00 · stock 30
    print(Producto.con_iva(producto.precio))  # 20 + 15 % de IVA = 23.0

    # 5) Venta: une un cliente con un producto usando sus ids.
    venta = Venta(100, cliente.id, producto.id, 2, producto.precio)
    producto.descontar_stock(venta.cantidad)  # se venden 2, el stock baja a 28
    print(venta)                              # muestra fecha, cliente, cantidad y total
    print("Stock que queda:", producto.stock)

    # 6) Método de CLASE: crea un objeto a partir de un diccionario.
    #    Es el camino inverso de a_diccionario().
    copia = cliente.desde_diccionario(cliente.a_diccionario())
    copia2 = Cliente.desde_diccionario(cliente.a_diccionario())
    print(copia)     # un Cliente nuevo, con los mismos datos
    print(copia2)  