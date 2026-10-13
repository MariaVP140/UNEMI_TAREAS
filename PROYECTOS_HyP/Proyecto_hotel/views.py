from abc import ABC, abstractmethod
from datetime import date
from models import Huesped, Habitacion, Reserva
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
# CONTROLADOR DE HUÉSPEDES
# =====================================================================
class HuespedController(CrudBase):
    def __init__(self, archivo="data/huespedes.json"):
        self.gestor = GestorJSON(archivo)
        # Leemos el JSON y convertimos cada diccionario en un objeto Huesped
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Huesped.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for huesped in self.lista:
            datos.append(huesped.a_diccionario())
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
            # CONJUNTO con los emails de los OTROS huéspedes
            usados = {huesped.email for huesped in self.lista if huesped.id != id_actual}
            if email in usados:
                return "Ese email ya está registrado"
        if "cedula" in datos:
            cedula = str(datos["cedula"]).strip()
            if cedula == "":
                return "La cédula no puede quedar vacía"
            if cedula in {huesped.cedula for huesped in self.lista if huesped.id != id_actual}:
                return f"La cédula {cedula} ya está registrada"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_huesped):
        for huesped in self.lista:
            if huesped.id == id_huesped:
                return huesped
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados
        for huesped in self.lista:
            if (texto in huesped.nombre.lower()
                    or texto in huesped.apellido.lower()
                    or texto in huesped.email.lower()
                    or texto in huesped.cedula.lower()):
                encontrados.append(huesped)
        return encontrados

    def siguiente(self):
        mayor = 0
        for huesped in self.lista:
            if huesped.id > mayor:
                mayor = huesped.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error
        huesped = Huesped(self.siguiente(),
                          str(datos["nombre"]).strip().title(),
                          str(datos["apellido"]).strip().title(),
                          str(datos["email"]).strip().lower(),
                          str(datos["cedula"]).strip(),
                          str(datos.get("telefono", "")).strip())
        self.lista.append(huesped)
        self.guardar()
        return True, f"Huésped creado: {huesped.etiqueta()}"

    def actualizar(self, id_huesped, datos):
        huesped = self.obtener(id_huesped)
        if huesped is None:
            return False, f"No existe un huésped con id {id_huesped}"
        if not datos:
            return False, "No se indicó ningún cambio"
        # DIFERENCIA de conjuntos: campos que no existen en un huésped
        permitidos = {"nombre", "apellido", "email", "cedula", "telefono"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        # Se valida ANTES de tocar el objeto: si algo falla, no cambia nada
        error = self.validar(datos, id_huesped)
        if error:
            return False, error
        for campo, valor in datos.items():
            valor = str(valor).strip()
            if campo in ("nombre", "apellido"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()
            setattr(huesped, campo, valor)
        self.guardar()
        return True, f"Huésped {id_huesped} actualizado"

    def eliminar(self, id_huesped):
        huesped = self.obtener(id_huesped)
        if huesped is None:
            return False, f"No existe un huésped con id {id_huesped}"
        self.lista.remove(huesped)
        self.guardar()
        return True, f"Huésped {id_huesped} eliminado"


# =====================================================================
# CONTROLADOR DE HABITACIONES
# =====================================================================
class HabitacionController(CrudBase):
    def __init__(self, archivo="data/habitaciones.json"):
        self.gestor = GestorJSON(archivo)
        # Leemos el JSON y convertimos cada diccionario en un objeto Habitacion
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Habitacion.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for habitacion in self.lista:
            datos.append(habitacion.a_diccionario())
        self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        """Devuelve un mensaje de error, o None si todo está bien."""
        # Al crear hay que traer los obligatorios; al actualizar, solo lo que cambia
        if id_actual is None:
            for campo in ("numero", "tipo", "precio_noche"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        if "numero" in datos:
            numero = str(datos["numero"]).strip()
            if numero == "":
                return "El número no puede quedar vacío"
            # CONJUNTO con los números de las OTRAS habitaciones
            if numero in {habitacion.numero for habitacion in self.lista if habitacion.id != id_actual}:
                return f"Ya existe la habitación {numero}"
        if "tipo" in datos and not Habitacion.es_tipo_valido(datos["tipo"]):
            return f"Tipo inválido. Use: {', '.join(Habitacion.TIPOS)}"
        if "precio_noche" in datos and not Habitacion.es_precio_valido(datos["precio_noche"]):
            return "El precio por noche debe ser un número mayor a 0"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_habitacion):
        for habitacion in self.lista:
            if habitacion.id == id_habitacion:
                return habitacion
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados
        for habitacion in self.lista:
            if (texto in habitacion.numero.lower()
                    or texto in habitacion.tipo.lower()):
                encontrados.append(habitacion)
        return encontrados

    def siguiente(self):
        mayor = 0
        for habitacion in self.lista:
            if habitacion.id > mayor:
                mayor = habitacion.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error
        habitacion = Habitacion(self.siguiente(),
                                str(datos["numero"]).strip(),
                                str(datos["tipo"]).strip().title(),
                                float(datos["precio_noche"]))
        self.lista.append(habitacion)
        self.guardar()
        return True, f"Habitación creada: {habitacion.etiqueta()}"

    def actualizar(self, id_habitacion, datos):
        habitacion = self.obtener(id_habitacion)
        if habitacion is None:
            return False, f"No existe una habitación con id {id_habitacion}"
        if not datos:
            return False, "No se indicó ningún cambio"
        # DIFERENCIA de conjuntos: campos que no existen en una habitación
        permitidos = {"numero", "tipo", "precio_noche"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        # Se valida ANTES de tocar el objeto: si algo falla, no cambia nada
        error = self.validar(datos, id_habitacion)
        if error:
            return False, error
        for campo, valor in datos.items():
            valor = str(valor).strip()
            if campo == "tipo":
                valor = valor.title()
            elif campo == "precio_noche":
                valor = float(valor)
            setattr(habitacion, campo, valor)
        self.guardar()
        return True, f"Habitación {id_habitacion} actualizada"

    def eliminar(self, id_habitacion):
        habitacion = self.obtener(id_habitacion)
        if habitacion is None:
            return False, f"No existe una habitación con id {id_habitacion}"
        self.lista.remove(habitacion)
        self.guardar()
        return True, f"Habitación {id_habitacion} eliminada"


# =====================================================================
# CONTROLADOR DE RESERVAS
# =====================================================================
class ReservaController(CrudBase):
    def __init__(self, huespedes, habitaciones, archivo="data/reservas.json"):
        # La reserva USA a los otros dos controladores.
        # Hay que pasarle los MISMOS que usa main.py.
        self.huespedes = huespedes
        self.habitaciones = habitaciones
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Reserva.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for reserva in self.lista:
            datos.append(reserva.a_diccionario())
        self.gestor.guardar(datos)

    def fechas_validas(self, entrada, salida):
        """Devuelve un mensaje de error, o None si el rango de fechas sirve."""
        try:
            dia_entrada = date.fromisoformat(entrada)
            date.fromisoformat(salida)
        except ValueError:
            return "Las fechas deben tener formato AAAA-MM-DD"
        if salida <= entrada:
            return "La salida debe ser posterior a la entrada"
        if dia_entrada < date.today():
            return "No se puede reservar en el pasado"
        return None

    def validar(self, datos):
        try:
            huesped_id = int(datos.get("huesped_id", 0))
            habitacion_id = int(datos.get("habitacion_id", 0))
        except (TypeError, ValueError):
            return "huesped_id y habitacion_id deben ser números enteros"
        entrada = str(datos.get("entrada", "")).strip()
        salida = str(datos.get("salida", "")).strip()
        error = self.fechas_validas(entrada, salida)
        if error:
            return error
        if self.huespedes.obtener(huesped_id) is None:
            return f"No existe un huésped con id {huesped_id}"
        if self.habitaciones.obtener(habitacion_id) is None:
            return f"No existe una habitación con id {habitacion_id}"
        # Cruce de fechas: dos reservas chocan si entrada < otra.salida y salida > otra.entrada
        for reserva in self.lista:
            if reserva.habitacion_id == habitacion_id and reserva.choca_con(entrada, salida):
                return f"La habitación ya está reservada del {reserva.entrada} al {reserva.salida}"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_reserva):
        for reserva in self.lista:
            if reserva.id == id_reserva:
                return reserva
        return None

    def buscar(self, texto):
        # Las reservas se buscan por fecha o estado, ej: "2026-10" o "cancelada"
        texto = texto.strip().lower()
        encontradas = []
        if texto == "":
            return encontradas
        for reserva in self.lista:
            if (texto in reserva.entrada or texto in reserva.salida
                    or texto in reserva.estado.lower()):
                encontradas.append(reserva)
        return encontradas

    def siguiente(self):
        mayor = 0
        for reserva in self.lista:
            if reserva.id > mayor:
                mayor = reserva.id
        return mayor + 1

    def crear(self, datos):
        # datos = {"huesped_id": 1, "habitacion_id": 2, "entrada": "2026-10-20", "salida": "2026-10-23"}
        error = self.validar(datos)
        if error:
            return False, error
        habitacion = self.habitaciones.obtener(int(datos["habitacion_id"]))
        reserva = Reserva(self.siguiente(),
                          int(datos["huesped_id"]),
                          habitacion.id,
                          str(datos["entrada"]).strip(),
                          str(datos["salida"]).strip(),
                          habitacion.precio_noche)      # foto del precio del momento
        self.lista.append(reserva)
        self.guardar()
        return True, f"Reserva {reserva.id}: {reserva.noches()} noches por ${reserva.calcular_total():.2f}"

    def actualizar(self, id_reserva, datos):
        # Una reserva registrada no se modifica: se cancela y se hace otra
        return False, "Una reserva no se modifica: cancélela y haga otra"

    def eliminar(self, id_reserva):
        """Cancelar una reserva: queda en el historial, pero libera las fechas."""
        reserva = self.obtener(id_reserva)
        if reserva is None:
            return False, f"No existe la reserva {id_reserva}"
        if reserva.estado == "Cancelada":
            return False, "Esa reserva ya estaba cancelada"
        reserva.estado = "Cancelada"
        self.guardar()
        return True, f"Reserva {id_reserva} cancelada. Las fechas quedaron libres"

    # --- propio de reservas ---
    def habitaciones_libres(self, entrada, salida):
        """Habitaciones sin cruce en ese rango. Devuelve None si las fechas no sirven."""
        try:
            date.fromisoformat(entrada)
            date.fromisoformat(salida)
        except ValueError:
            return None
        if salida <= entrada:
            return None
        # CONJUNTO con los ids de las habitaciones ocupadas en ese rango
        ocupadas = {r.habitacion_id for r in self.lista if r.choca_con(entrada, salida)}
        libres = []
        for habitacion in self.habitaciones.leer():
            if habitacion.id not in ocupadas:
                libres.append(habitacion)
        return libres

    def comprobante(self, id_reserva):
        reserva = self.obtener(id_reserva)
        if reserva is None:
            return None
        # DICCIONARIOS ÍNDICE {id: objeto}
        huespedes = {h.id: h for h in self.huespedes.leer()}
        habitaciones = {h.id: h for h in self.habitaciones.leer()}
        huesped = huespedes.get(reserva.huesped_id)
        habitacion = habitaciones.get(reserva.habitacion_id)
        subtotal = reserva.calcular_total()
        texto = f"RESERVA #{reserva.id}   ({reserva.estado})\n"
        texto += f"Huésped   : {huesped.nombre_completo() if huesped else 'eliminado'}\n"
        if habitacion:
            texto += f"Habitación: {habitacion.numero} · {habitacion.tipo}\n"
        else:
            texto += "Habitación: eliminada\n"
        texto += (f"Estadía   : {reserva.entrada} → {reserva.salida}  "
                  f"({reserva.noches()} noches x ${reserva.precio_noche:.2f})\n")
        texto += "-" * 42 + "\n"
        texto += f"SUBTOTAL: ${subtotal:.2f}\n"
        texto += f"TOTAL con IVA: ${Habitacion.con_iva(subtotal):.2f}"
        return texto

    def reservas_por_huesped(self):
        """DICCIONARIO de LISTAS: {huesped_id: [reservas de ese huésped]}."""
        agrupadas = {}
        for reserva in self.lista:
            agrupadas.setdefault(reserva.huesped_id, []).append(reserva)
        return agrupadas

    def total_activas(self):
        total = 0
        for reserva in self.lista:
            if reserva.estado == "Activa":
                total += 1
        return total

    def ingresos_esperados(self):
        total = 0.0
        for reserva in self.lista:
            if reserva.estado == "Activa":
                total += reserva.calcular_total()
        return round(total, 2)
