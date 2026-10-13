from abc import ABC, abstractmethod
from datetime import date
from models import Socio, Libro, Prestamo
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido

# =====================================================================
# CLASE BASE (ABSTRACTA)
# =====================================================================
# Solo dice QUÉ métodos debe tener todo controlador.
# CÓMO se hace cada uno lo escribe cada controlador, de la forma más simple.
class CrudBase(ABC):
    @abstractmethod
    def leer(self):
        pass

    @abstractmethod
    def obtener(self, id_registro):
        pass

    @abstractmethod
    def buscar(self, texto):
        pass

    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod
    def crear(self, datos):
        pass

    @abstractmethod
    def actualizar(self, id_registro, datos):
        pass

    @abstractmethod
    def eliminar(self, id_registro):
        pass


# =====================================================================
# CONTROLADOR DE SOCIOS
# =====================================================================
class SocioController(CrudBase):
    def __init__(self, archivo="data/socios.json"):
        self.gestor = GestorJSON(archivo)
        # Leemos el JSON y convertimos cada diccionario en un objeto Socio
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Socio.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for socio in self.lista:
            datos.append(socio.a_diccionario())
        self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        """Devuelve un mensaje de error, o None si todo está bien."""
        # Al crear hay que traer los obligatorios; al actualizar, solo lo que cambia
        if id_actual is None:
            for campo in ("nombre", "apellido", "email", "cedula"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        if "email" in datos:
            email = str(datos["email"]).strip().lower()
            if not es_email_valido(email):
                return f"Email inválido: '{email}'"
            # CONJUNTO con los emails de los OTROS socios
            usados = {socio.email for socio in self.lista if socio.id != id_actual}
            if email in usados:
                return "Ese email ya está registrado"
        if "cedula" in datos:
            cedula = str(datos["cedula"]).strip()
            if cedula == "":
                return "La cédula no puede quedar vacía"
            if cedula in {socio.cedula for socio in self.lista if socio.id != id_actual}:
                return f"La cédula {cedula} ya está registrada"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_socio):
        for socio in self.lista:
            if socio.id == id_socio:
                return socio
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados
        for socio in self.lista:
            if (texto in socio.nombre.lower()
                    or texto in socio.apellido.lower()
                    or texto in socio.email.lower()
                    or texto in socio.cedula.lower()):
                encontrados.append(socio)
        return encontrados

    def siguiente(self):
        mayor = 0
        for socio in self.lista:
            if socio.id > mayor:
                mayor = socio.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error
        socio = Socio(self.siguiente(),
                      str(datos["nombre"]).strip().title(),
                      str(datos["apellido"]).strip().title(),
                      str(datos["email"]).strip().lower(),
                      str(datos["cedula"]).strip(),
                      str(datos.get("telefono", "")).strip())
        self.lista.append(socio)
        self.guardar()
        return True, f"Socio creado: {socio.etiqueta()}"

    def actualizar(self, id_socio, datos):
        socio = self.obtener(id_socio)
        if socio is None:
            return False, f"No existe un socio con id {id_socio}"
        if not datos:
            return False, "No se indicó ningún cambio"
        # DIFERENCIA de conjuntos: campos que no existen en un socio
        permitidos = {"nombre", "apellido", "email", "cedula", "telefono"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        # Se valida ANTES de tocar el objeto: si algo falla, no cambia nada
        error = self.validar(datos, id_socio)
        if error:
            return False, error
        for campo, valor in datos.items():
            valor = str(valor).strip()
            if campo in ("nombre", "apellido"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()
            setattr(socio, campo, valor)
        self.guardar()
        return True, f"Socio {id_socio} actualizado"

    def eliminar(self, id_socio):
        socio = self.obtener(id_socio)
        if socio is None:
            return False, f"No existe un socio con id {id_socio}"
        self.lista.remove(socio)
        self.guardar()
        return True, f"Socio {id_socio} eliminado"


# =====================================================================
# CONTROLADOR DE LIBROS
# =====================================================================
class LibroController(CrudBase):
    def __init__(self, archivo="data/libros.json"):
        self.gestor = GestorJSON(archivo)
        # Leemos el JSON y convertimos cada diccionario en un objeto Libro
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Libro.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for libro in self.lista:
            datos.append(libro.a_diccionario())
        self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        """Devuelve un mensaje de error, o None si todo está bien."""
        # Al crear hay que traer los obligatorios; al actualizar, solo lo que cambia
        if id_actual is None:
            for campo in ("titulo", "autor", "isbn"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        if "isbn" in datos:
            if not Libro.es_isbn_valido(datos["isbn"]):
                return "El ISBN debe tener 10 o 13 dígitos"
            isbn = str(datos["isbn"]).replace("-", "").strip()
            # CONJUNTO con los ISBN de los OTROS libros
            if isbn in {libro.isbn for libro in self.lista if libro.id != id_actual}:
                return "Ese ISBN ya está registrado"
        copias = str(datos.get("copias", "")).strip()
        if copias != "" and not copias.isdigit():
            return "Las copias deben ser un entero mayor o igual a 0"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_libro):
        for libro in self.lista:
            if libro.id == id_libro:
                return libro
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados
        for libro in self.lista:
            if (texto in libro.titulo.lower()
                    or texto in libro.autor.lower()
                    or texto in libro.isbn.lower()):
                encontrados.append(libro)
        return encontrados

    def siguiente(self):
        mayor = 0
        for libro in self.lista:
            if libro.id > mayor:
                mayor = libro.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error
        libro = Libro(self.siguiente(),
                      str(datos["titulo"]).strip().title(),
                      str(datos["autor"]).strip().title(),
                      str(datos["isbn"]).replace("-", "").strip(),
                      int(str(datos.get("copias", "")).strip() or 0))
        self.lista.append(libro)
        self.guardar()
        return True, f"Libro creado: {libro.etiqueta()}"

    def actualizar(self, id_libro, datos):
        libro = self.obtener(id_libro)
        if libro is None:
            return False, f"No existe un libro con id {id_libro}"
        if not datos:
            return False, "No se indicó ningún cambio"
        # DIFERENCIA de conjuntos: campos que no existen en un libro
        permitidos = {"titulo", "autor", "isbn", "copias"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        # Se valida ANTES de tocar el objeto: si algo falla, no cambia nada
        error = self.validar(datos, id_libro)
        if error:
            return False, error
        for campo, valor in datos.items():
            valor = str(valor).strip()
            if campo in ("titulo", "autor"):
                valor = valor.title()
            elif campo == "isbn":
                valor = valor.replace("-", "")
            elif campo == "copias":
                valor = int(valor)
            setattr(libro, campo, valor)
        self.guardar()
        return True, f"Libro {id_libro} actualizado"

    def eliminar(self, id_libro):
        libro = self.obtener(id_libro)
        if libro is None:
            return False, f"No existe un libro con id {id_libro}"
        self.lista.remove(libro)
        self.guardar()
        return True, f"Libro {id_libro} eliminado"

    # --- propio de libros ---
    def sin_copias(self):
        agotados = []
        for libro in self.lista:
            if not libro.hay_copia():
                agotados.append(libro)
        return agotados


# =====================================================================
# CONTROLADOR DE PRÉSTAMOS
# =====================================================================
class PrestamoController(CrudBase):
    def __init__(self, socios, libros, archivo="data/prestamos.json"):
        # El préstamo USA a los otros dos controladores.
        # Hay que pasarle los MISMOS que usa main.py.
        self.socios = socios
        self.libros = libros
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Prestamo.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for prestamo in self.lista:
            datos.append(prestamo.a_diccionario())
        self.gestor.guardar(datos)

    def fecha_valida(self, texto):
        try:
            date.fromisoformat(texto)
            return True
        except ValueError:
            return False

    def validar(self, datos):
        try:
            socio_id = int(datos.get("socio_id", 0))
            libro_id = int(datos.get("libro_id", 0))
        except (TypeError, ValueError):
            return "socio_id y libro_id deben ser números enteros"
        # La fecha es opcional: sirve para registrar préstamos de días pasados
        if datos.get("fecha") and not self.fecha_valida(datos["fecha"]):
            return "La fecha debe tener formato AAAA-MM-DD"
        if self.socios.obtener(socio_id) is None:
            return f"No existe un socio con id {socio_id}"
        libro = self.libros.obtener(libro_id)
        if libro is None:
            return f"No existe un libro con id {libro_id}"
        if not libro.hay_copia():
            return f"No quedan copias de '{libro.titulo}'"
        activos = []
        for prestamo in self.lista:
            if prestamo.socio_id == socio_id and prestamo.esta_activo():
                activos.append(prestamo)
        if len(activos) >= Libro.MAX_PRESTAMOS:
            return f"El socio ya tiene {Libro.MAX_PRESTAMOS} préstamos activos"
        # CONJUNTO con los libros que el socio todavía tiene
        if libro_id in {prestamo.libro_id for prestamo in activos}:
            return "El socio ya tiene ese libro prestado"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_prestamo):
        for prestamo in self.lista:
            if prestamo.id == id_prestamo:
                return prestamo
        return None

    def buscar(self, texto):
        # Los préstamos se buscan por fecha o estado, ej: "2026-09" o "atrasado"
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados
        for prestamo in self.lista:
            if texto in prestamo.fecha_prestamo or texto in prestamo.estado().lower():
                encontrados.append(prestamo)
        return encontrados

    def siguiente(self):
        mayor = 0
        for prestamo in self.lista:
            if prestamo.id > mayor:
                mayor = prestamo.id
        return mayor + 1

    def crear(self, datos):
        # datos = {"socio_id": 1, "libro_id": 2}   (y opcional "fecha")
        error = self.validar(datos)
        if error:
            return False, error
        libro = self.libros.obtener(int(datos["libro_id"]))
        prestamo = Prestamo(self.siguiente(),
                            int(datos["socio_id"]),
                            libro.id,
                            str(datos.get("fecha", "")).strip())
        libro.prestar_copia()
        self.libros.guardar()                   # guarda las copias nuevas en libros.json
        self.lista.append(prestamo)
        self.guardar()
        return True, f"Préstamo {prestamo.id}: devolver antes del {prestamo.fecha_limite()}"

    def devolver(self, id_prestamo, fecha=""):
        """Registrar la devolución: el libro vuelve y se calcula la multa."""
        prestamo = self.obtener(id_prestamo)
        if prestamo is None:
            return False, f"No existe el préstamo {id_prestamo}"
        if not prestamo.esta_activo():
            return False, "Ese préstamo ya fue devuelto"
        if fecha and not self.fecha_valida(fecha):
            return False, "La fecha debe tener formato AAAA-MM-DD"
        prestamo.fecha_devolucion = fecha or date.today().isoformat()
        libro = self.libros.obtener(prestamo.libro_id)
        if libro is not None:
            libro.recibir_copia()
            self.libros.guardar()
        self.guardar()
        multa = prestamo.multa()
        if multa > 0:
            return True, f"Devuelto con {prestamo.dias_atraso()} días de atraso. Multa: ${multa:.2f}"
        return True, "Devuelto a tiempo. Sin multa"

    def actualizar(self, id_prestamo, datos):
        # Un préstamo registrado no se modifica: se registra su devolución
        return False, "Un préstamo no se modifica: registre la devolución"

    def eliminar(self, id_prestamo):
        # Los préstamos son historial: no se borran
        return False, "Los préstamos no se borran: use devolver()"

    # --- propio de préstamos ---
    def ficha_prestamo(self, id_prestamo):
        prestamo = self.obtener(id_prestamo)
        if prestamo is None:
            return None
        # DICCIONARIOS ÍNDICE {id: objeto}
        socios = {s.id: s for s in self.socios.leer()}
        libros = {l.id: l for l in self.libros.leer()}
        socio = socios.get(prestamo.socio_id)
        libro = libros.get(prestamo.libro_id)
        texto = f"PRÉSTAMO #{prestamo.id}   estado: {prestamo.estado()}\n"
        texto += f"Socio   : {socio.nombre_completo() if socio else 'eliminado'}\n"
        texto += f"Libro   : {libro.titulo if libro else 'eliminado'}\n"
        texto += f"Prestado: {prestamo.fecha_prestamo}   Límite: {prestamo.fecha_limite()}\n"
        if prestamo.fecha_devolucion:
            texto += f"Devuelto: {prestamo.fecha_devolucion}\n"
        texto += "-" * 42 + "\n"
        texto += f"Días de atraso: {prestamo.dias_atraso()}\n"
        texto += f"MULTA: ${prestamo.multa():.2f}"
        return texto

    def activos_por_socio(self):
        """DICCIONARIO de LISTAS: {socio_id: [préstamos activos de ese socio]}."""
        agrupados = {}
        for prestamo in self.lista:
            if prestamo.esta_activo():
                agrupados.setdefault(prestamo.socio_id, []).append(prestamo)
        return agrupados

    def atrasados(self):
        atrasados = []
        for prestamo in self.lista:
            if prestamo.estado() == "Atrasado":
                atrasados.append(prestamo)
        return atrasados

    def total_multas(self):
        total = 0.0
        for prestamo in self.lista:
            total += prestamo.multa()
        return round(total, 2)
