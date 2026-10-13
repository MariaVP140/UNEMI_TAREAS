from datetime import date, timedelta


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


class Socio(Persona):
    """Socio ES UNA Persona, con cédula y teléfono."""

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
class Libro(ModeloBase):
    """Libro ES UN ModeloBase. Aquí vive todo lo estático del proyecto."""

    # ATRIBUTOS ESTÁTICOS (de clase)
    DIAS_PRESTAMO = 7         # días que se puede tener un libro
    MULTA_POR_DIA = 0.50      # dólares por cada día de atraso
    MAX_PRESTAMOS = 3         # préstamos activos por socio

    def __init__(self, id_registro, titulo, autor, isbn, copias=0):
        super().__init__(id_registro)
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias = int(copias)

    # MÉTODO ESTÁTICO: regla que no necesita ningún libro concreto
    @staticmethod
    def es_isbn_valido(valor):
        limpio = str(valor).replace("-", "").strip()
        return limpio.isdigit() and len(limpio) in (10, 13)

    # MÉTODOS DE INSTANCIA
    def hay_copia(self):
        return self.copias > 0

    def prestar_copia(self):
        self.copias -= 1

    def recibir_copia(self):
        self.copias += 1

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["titulo"] = self.titulo
        datos["autor"] = self.autor
        datos["isbn"] = self.isbn
        datos["copias"] = self.copias
        return datos

    def etiqueta(self):
        aviso = " ⚠ sin copias" if not self.hay_copia() else ""
        return f"{self.titulo} · {self.autor} · copias {self.copias}{aviso}"


# =====================================================================
class Prestamo(ModeloBase):
    """Préstamo: un socio se lleva un libro y lo devuelve después."""

    def __init__(self, id_registro, socio_id, libro_id, fecha_prestamo="",
                 fecha_devolucion=None):
        super().__init__(id_registro)
        self.socio_id = int(socio_id)
        self.libro_id = int(libro_id)
        self.fecha_prestamo = fecha_prestamo or date.today().isoformat()
        # None significa que el socio todavía tiene el libro
        self.fecha_devolucion = fecha_devolucion or None

    # --- cálculos con FECHAS (date.fromisoformat + timedelta) ---
    def fecha_limite(self):
        inicio = date.fromisoformat(self.fecha_prestamo)
        return inicio + timedelta(days=Libro.DIAS_PRESTAMO)

    def esta_activo(self):
        return self.fecha_devolucion is None

    def dias_atraso(self, hoy=None):
        if self.fecha_devolucion:
            fin = date.fromisoformat(self.fecha_devolucion)
        else:
            fin = hoy or date.today()
        return max(0, (fin - self.fecha_limite()).days)

    def multa(self, hoy=None):
        # Se calcula cada vez; NO se guarda, para que nunca quede desactualizada
        return round(self.dias_atraso(hoy) * Libro.MULTA_POR_DIA, 2)

    def estado(self, hoy=None):
        if not self.esta_activo():
            return "Devuelto"
        return "Atrasado" if self.dias_atraso(hoy) > 0 else "Activo"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["socio_id"] = self.socio_id
        datos["libro_id"] = self.libro_id
        datos["fecha_prestamo"] = self.fecha_prestamo
        datos["fecha_devolucion"] = self.fecha_devolucion
        return datos

    def etiqueta(self):
        return (f"socio {self.socio_id} · libro {self.libro_id} · "
                f"{self.fecha_prestamo} → límite {self.fecha_limite()} "
                f"({self.estado()})")
