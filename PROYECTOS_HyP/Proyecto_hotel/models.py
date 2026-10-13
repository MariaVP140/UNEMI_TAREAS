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
        cls es la clase que llamó: Estudiante, Materia o Matricula."""
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

    def __str__(self):
        # Lo que se ve al hacer print(objeto). Llama a etiqueta(),
        # así que cada modelo se imprime distinto sin cambiar esta línea.
        return f"[{self.id}] {self.etiqueta()}"


# =====================================================================
# HERENCIA: Persona es la base de las clases que son personas
# =====================================================================
class Persona(ModeloBase):
    """Todo lo que tiene una persona del sistema."""

    def __init__(self, id_registro, nombre, apellido, email):
        super().__init__(id_registro)      # el padre guarda el id
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


class Huesped(Persona):
    """Huésped ES UNA Persona, con cédula y teléfono."""

    def __init__(self, id_registro, nombre, apellido, email, cedula="", telefono=""):
        super().__init__(id_registro, nombre, apellido, email)
        self.cedula = cedula
        self.telefono = telefono

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["cedula"] = self.cedula
        datos["telefono"] = self.telefono
        return datos

    def etiqueta(self):
        return f"{super().etiqueta()} · {self.cedula}"


# =====================================================================
# ÚNICA CLASE CON ATRIBUTOS Y MÉTODOS ESTÁTICOS
# =====================================================================
class Habitacion(ModeloBase):
    """Habitación ES UN ModeloBase. Aquí vive todo lo estático del proyecto."""

    # ATRIBUTOS ESTÁTICOS (de clase)
    TIPOS = ("Simple", "Doble", "Suite")     # TUPLA fija
    IVA = 0.15                               # 15 %

    def __init__(self, id_registro, numero, tipo, precio_noche):
        super().__init__(id_registro)
        self.numero = str(numero)
        self.tipo = tipo
        self.precio_noche = float(precio_noche)

    # MÉTODOS ESTÁTICOS: reglas que no necesitan ninguna habitación concreta
    @staticmethod
    def es_tipo_valido(valor):
        return str(valor).strip().title() in Habitacion.TIPOS

    @staticmethod
    def es_precio_valido(valor):
        try:
            return float(valor) > 0
        except (TypeError, ValueError):
            return False

    @staticmethod
    def con_iva(monto):
        return round(monto * (1 + Habitacion.IVA), 2)

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["numero"] = self.numero
        datos["tipo"] = self.tipo
        datos["precio_noche"] = self.precio_noche
        return datos

    def etiqueta(self):
        return f"Hab. {self.numero} · {self.tipo} · ${self.precio_noche:.2f}/noche"


# =====================================================================
class Reserva(ModeloBase):
    """Reserva: un huésped, una habitación, de una fecha de entrada a una de salida."""

    def __init__(self, id_registro, huesped_id, habitacion_id, entrada, salida,
                 precio_noche, estado="Activa"):
        super().__init__(id_registro)
        self.huesped_id = int(huesped_id)
        self.habitacion_id = int(habitacion_id)
        self.entrada = entrada                    # "AAAA-MM-DD"
        self.salida = salida
        self.precio_noche = float(precio_noche)   # foto del precio del momento
        self.estado = estado                      # "Activa" o "Cancelada"

    def noches(self):
        dias = date.fromisoformat(self.salida) - date.fromisoformat(self.entrada)
        return dias.days

    def calcular_total(self):
        # Se calcula cada vez; NO se guarda
        return round(self.noches() * self.precio_noche, 2)

    def choca_con(self, entrada, salida):
        """True si esta reserva (activa) se cruza con el rango pedido.
        Las fechas ISO se comparan bien como texto: '2026-10-05' < '2026-10-07'."""
        return self.estado == "Activa" and entrada < self.salida and salida > self.entrada

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["huesped_id"] = self.huesped_id
        datos["habitacion_id"] = self.habitacion_id
        datos["entrada"] = self.entrada
        datos["salida"] = self.salida
        datos["precio_noche"] = self.precio_noche
        datos["estado"] = self.estado
        return datos

    def etiqueta(self):
        return (f"huésped {self.huesped_id} · hab {self.habitacion_id} · "
                f"{self.entrada} → {self.salida} "
                f"({self.noches()} noches, {self.estado})")
