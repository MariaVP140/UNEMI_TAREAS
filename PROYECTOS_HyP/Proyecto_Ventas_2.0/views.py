from abc import ABC, abstractmethod

from models import Estudiante, Profesor, Materia, Matricula
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
# CONTROLADOR DE ESTUDIANTES
# =====================================================================
class EstudianteController(CrudBase):
    def __init__(self, archivo="data/estudiantes.json"):
        self.gestor = GestorJSON(archivo)
        # Leemos el JSON y convertimos cada diccionario en un objeto Estudiante
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Estudiante.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for estudiante in self.lista:
            datos.append(estudiante.a_diccionario())
        self.gestor.guardar(datos)

    def carnets_registrados(self, excepto_id=None):
        """CONJUNTO de carnets ya usados: preguntar 'x in conjunto' es instantáneo."""
        return {e.carnet.upper() for e in self.lista if e.id != excepto_id}

    def validar(self, datos, id_actual=None):
        """Devuelve un mensaje de error, o None si todo está bien."""
        # Al crear hay que traer los cuatro obligatorios; al actualizar, solo lo que cambia
        if id_actual is None:
            for campo in ("nombre", "apellido", "email", "carnet"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        if "email" in datos:
            email = str(datos["email"]).strip().lower()
            if not es_email_valido(email):
                return f"Email inválido: '{email}'"
            # CONJUNTO con los emails de los OTROS estudiantes
            usados = {e.email for e in self.lista if e.id != id_actual}
            if email in usados:
                return "Ese email ya está registrado"
        if "carnet" in datos:
            carnet = str(datos["carnet"]).strip().upper()
            if carnet == "":
                return "El carnet no puede quedar vacío"
            if carnet in self.carnets_registrados(id_actual):
                return f"El carnet {carnet} ya está registrado"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_estudiante):
        for estudiante in self.lista:
            if estudiante.id == id_estudiante:
                return estudiante
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados
        for estudiante in self.lista:
            if (texto in estudiante.nombre.lower()
                    or texto in estudiante.apellido.lower()
                    or texto in estudiante.email
                    or texto in estudiante.carnet.lower()
                    or texto in estudiante.carrera.lower()):
                encontrados.append(estudiante)
        return encontrados

    def siguiente(self):
        mayor = 0
        for estudiante in self.lista:
            if estudiante.id > mayor:
                mayor = estudiante.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error
        estudiante = Estudiante(self.siguiente(),
                                str(datos["nombre"]).strip().title(),
                                str(datos["apellido"]).strip().title(),
                                str(datos["email"]).strip().lower(),
                                str(datos["carnet"]).strip().upper(),
                                str(datos.get("carrera", "")).strip().title())
        self.lista.append(estudiante)
        self.guardar()
        return True, f"Estudiante creado: {estudiante.etiqueta()}"

    def actualizar(self, id_estudiante, datos):
        estudiante = self.obtener(id_estudiante)
        if estudiante is None:
            return False, f"No existe un estudiante con id {id_estudiante}"
        if not datos:
            return False, "No se indicó ningún cambio"
        # DIFERENCIA de conjuntos: campos que no existen en un estudiante
        permitidos = {"nombre", "apellido", "email", "carnet", "carrera"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        # Se valida ANTES de tocar el objeto: si algo falla, no cambia nada
        error = self.validar(datos, id_estudiante)
        if error:
            return False, error
        for campo, valor in datos.items():
            valor = str(valor).strip()
            if campo in ("nombre", "apellido", "carrera"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()
            elif campo == "carnet":
                valor = valor.upper()
            setattr(estudiante, campo, valor)
        self.guardar()
        return True, f"Estudiante {id_estudiante} actualizado"

    def eliminar(self, id_estudiante):
        estudiante = self.obtener(id_estudiante)
        if estudiante is None:
            return False, f"No existe un estudiante con id {id_estudiante}"
        self.lista.remove(estudiante)
        self.guardar()
        return True, f"Estudiante {id_estudiante} eliminado"

    # --- propio de estudiantes ---
    def carreras(self):
        """CONJUNTO de carreras: sin repetidas. sorted() lo devuelve como lista."""
        return sorted({e.carrera for e in self.lista if e.carrera != ""})


# =====================================================================
# CONTROLADOR DE PROFESORES
# =====================================================================
class ProfesorController(CrudBase):
    def __init__(self, archivo="data/profesores.json"):
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Profesor.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for profesor in self.lista:
            datos.append(profesor.a_diccionario())
        self.gestor.guardar(datos)

    def cedulas_registradas(self, excepto_id=None):
        """CONJUNTO de cédulas ya usadas: preguntar 'x in conjunto' es instantáneo."""
        return {p.cedula for p in self.lista if p.id != excepto_id}

    def validar(self, datos, id_actual=None):
        """Devuelve un mensaje de error, o None si todo está bien."""
        if id_actual is None:
            for campo in ("nombre", "apellido", "email", "cedula"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        if "email" in datos:
            email = str(datos["email"]).strip().lower()
            if not es_email_valido(email):
                return f"Email inválido: '{email}'"
            # CONJUNTO con los emails de los OTROS profesores
            usados = {p.email for p in self.lista if p.id != id_actual}
            if email in usados:
                return "Ese email ya está registrado"
        if "cedula" in datos:
            cedula = str(datos["cedula"]).strip()
            if cedula == "":
                return "La cédula no puede quedar vacía"
            if cedula in self.cedulas_registradas(id_actual):
                return f"La cédula {cedula} ya está registrada"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_profesor):
        for profesor in self.lista:
            if profesor.id == id_profesor:
                return profesor
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados
        for profesor in self.lista:
            if (texto in profesor.nombre.lower()
                    or texto in profesor.apellido.lower()
                    or texto in profesor.email
                    or texto in profesor.cedula
                    or texto in profesor.especialidad.lower()):
                encontrados.append(profesor)
        return encontrados

    def siguiente(self):
        mayor = 0
        for profesor in self.lista:
            if profesor.id > mayor:
                mayor = profesor.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error
        profesor = Profesor(self.siguiente(),
                            str(datos["nombre"]).strip().title(),
                            str(datos["apellido"]).strip().title(),
                            str(datos["email"]).strip().lower(),
                            str(datos["cedula"]).strip(),
                            str(datos.get("especialidad", "")).strip().title())
        self.lista.append(profesor)
        self.guardar()
        return True, f"Profesor creado: {profesor.etiqueta()}"

    def actualizar(self, id_profesor, datos):
        profesor = self.obtener(id_profesor)
        if profesor is None:
            return False, f"No existe un profesor con id {id_profesor}"
        if not datos:
            return False, "No se indicó ningún cambio"
        # DIFERENCIA de conjuntos: campos que no existen en un profesor
        permitidos = {"nombre", "apellido", "email", "cedula", "especialidad"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        # Se valida ANTES de tocar el objeto: si algo falla, no cambia nada
        error = self.validar(datos, id_profesor)
        if error:
            return False, error
        for campo, valor in datos.items():
            valor = str(valor).strip()
            if campo in ("nombre", "apellido", "especialidad"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()
            setattr(profesor, campo, valor)
        self.guardar()
        return True, f"Profesor {id_profesor} actualizado"

    def eliminar(self, id_profesor):
        profesor = self.obtener(id_profesor)
        if profesor is None:
            return False, f"No existe un profesor con id {id_profesor}"
        self.lista.remove(profesor)
        self.guardar()
        return True, f"Profesor {id_profesor} eliminado"

    # --- propio de profesores ---
    def especialidades(self):
        """CONJUNTO de especialidades: sin repetidas. sorted() lo devuelve como lista."""
        return sorted({p.especialidad for p in self.lista if p.especialidad != ""})


# =====================================================================
# CONTROLADOR DE MATERIAS
# =====================================================================
class MateriaController(CrudBase):
    def __init__(self, profesores, archivo="data/materias.json"):
        # La materia USA al controlador de profesores para comprobar que el id exista
        self.profesores = profesores
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Materia.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for materia in self.lista:
            datos.append(materia.a_diccionario())
        self.gestor.guardar(datos)

    def codigos_registrados(self, excepto_id=None):
        """CONJUNTO de códigos ya usados: preguntar 'x in conjunto' es instantáneo."""
        return {m.codigo.upper() for m in self.lista if m.id != excepto_id}

    def validar(self, datos, id_actual=None):
        if id_actual is None:
            for campo in ("nombre", "codigo", "creditos"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        if "codigo" in datos:
            codigo = str(datos["codigo"]).strip().upper()
            if codigo == "":
                return "El código no puede quedar vacío"
            if codigo in self.codigos_registrados(id_actual):
                return f"El código {codigo} ya está registrado"
        if "creditos" in datos:
            creditos = str(datos["creditos"]).strip()
            if not creditos.isdigit() or not 1 <= int(creditos) <= 10:
                return "Los créditos deben ser un entero entre 1 y 10"
        cupos = str(datos.get("cupos", "")).strip()
        if cupos != "":
            if not cupos.isdigit() or int(cupos) > Materia.CUPOS_MAXIMOS:
                return f"Los cupos deben ser un entero entre 0 y {Materia.CUPOS_MAXIMOS}"
        # Profesor: vacío o 0 = sin profesor; cualquier otro id debe existir
        profesor_id = str(datos.get("profesor_id", "")).strip()
        if profesor_id != "":
            if not profesor_id.isdigit():
                return "El id del profesor debe ser un número entero"
            # CONJUNTO de ids: saber si un id existe es instantáneo
            ids_profesores = {p.id for p in self.profesores.leer()}
            if int(profesor_id) != 0 and int(profesor_id) not in ids_profesores:
                return f"No existe un profesor con id {profesor_id}"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_materia):
        for materia in self.lista:
            if materia.id == id_materia:
                return materia
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontradas = []
        if texto == "":
            return encontradas
        for materia in self.lista:
            if texto in materia.nombre.lower() or texto in materia.codigo.lower():
                encontradas.append(materia)
        return encontradas

    def siguiente(self):
        mayor = 0
        for materia in self.lista:
            if materia.id > mayor:
                mayor = materia.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error
        # Si no escribieron los cupos, empieza en 0
        cupos = str(datos.get("cupos", "")).strip()
        profesor_id = str(datos.get("profesor_id", "")).strip()
        materia = Materia(self.siguiente(),
                          str(datos["nombre"]).strip().title(),
                          str(datos["codigo"]).strip().upper(),
                          int(datos["creditos"]),
                          int(cupos) if cupos != "" else 0,
                          int(profesor_id) if profesor_id != "" else 0)
        self.lista.append(materia)
        self.guardar()
        return True, f"Materia creada: {materia.etiqueta()}"

    def actualizar(self, id_materia, datos):
        materia = self.obtener(id_materia)
        if materia is None:
            return False, f"No existe una materia con id {id_materia}"
        if not datos:
            return False, "No se indicó ningún cambio"
        desconocidos = set(datos) - {"nombre", "codigo", "creditos", "cupos", "profesor_id"}
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos, id_materia)
        if error:
            return False, error
        if "nombre" in datos:
            materia.nombre = str(datos["nombre"]).strip().title()
        if "codigo" in datos:
            materia.codigo = str(datos["codigo"]).strip().upper()
        if "creditos" in datos:
            materia.creditos = int(datos["creditos"])
        if "cupos" in datos:
            materia.cupos = int(datos["cupos"])
        if "profesor_id" in datos:
            materia.profesor_id = int(datos["profesor_id"])
        self.guardar()
        return True, f"Materia {id_materia} actualizada"

    def eliminar(self, id_materia):
        materia = self.obtener(id_materia)
        if materia is None:
            return False, f"No existe una materia con id {id_materia}"
        self.lista.remove(materia)
        self.guardar()
        return True, f"Materia {id_materia} eliminada"

    # --- propio de materias ---
    def materias_de_profesor(self, id_profesor):
        dictadas = []
        for materia in self.lista:
            if materia.profesor_id == id_profesor:
                dictadas.append(materia)
        return dictadas

    def materias_sin_cupo(self):
        sin_cupo = []
        for materia in self.lista:
            if not materia.hay_cupo():
                sin_cupo.append(materia)
        return sin_cupo


# =====================================================================
# CONTROLADOR DE MATRÍCULAS
# =====================================================================
class MatriculaController(CrudBase):
    def __init__(self, estudiantes, materias, profesores, archivo="data/matriculas.json"):
        # La matrícula USA a los otros tres controladores.
        # Hay que pasarle los MISMOS que usa main.py.
        self.estudiantes = estudiantes
        self.materias = materias
        self.profesores = profesores
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Matricula.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for matricula in self.lista:
            datos.append(matricula.a_diccionario())
        self.gestor.guardar(datos)

    def periodo_valido(self, texto):
        # Formato AAAA-N, por ejemplo 2026-1
        partes = texto.strip().split("-")
        if len(partes) != 2:
            return False
        anio, numero = partes
        return (len(anio) == 4 and anio.isdigit()
                and numero.isdigit() and 1 <= int(numero) <= 4)

    def validar(self, datos):
        try:
            estudiante_id = int(datos.get("estudiante_id", 0))
            materia_id = int(datos.get("materia_id", 0))
        except (TypeError, ValueError):
            return "estudiante_id y materia_id deben ser números enteros"
        periodo = str(datos.get("periodo", "")).strip()
        if not self.periodo_valido(periodo):
            return "Periodo inválido: use el formato AAAA-N, por ejemplo 2026-1"
        # CONJUNTOS de ids: saber si un id existe es instantáneo
        ids_estudiantes = {e.id for e in self.estudiantes.leer()}
        ids_materias = {m.id for m in self.materias.leer()}
        if estudiante_id not in ids_estudiantes:
            return f"No existe un estudiante con id {estudiante_id}"
        if materia_id not in ids_materias:
            return f"No existe una materia con id {materia_id}"
        materia = self.materias.obtener(materia_id)
        if not materia.hay_cupo():
            return f"La materia {materia.nombre} no tiene cupos disponibles"
        # Estudiante, materia y periodo se comparan JUNTOS, no por separado
        for m in self.lista:
            if (m.estudiante_id == estudiante_id
                    and m.materia_id == materia_id
                    and m.periodo == periodo):
                return "El estudiante ya está matriculado en esa materia en ese periodo"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_matricula):
        for matricula in self.lista:
            if matricula.id == id_matricula:
                return matricula
        return None

    def buscar(self, texto):
        # Las matrículas se buscan por periodo o fecha, ej: "2026-1"
        texto = texto.strip()
        encontradas = []
        if texto == "":
            return encontradas
        for matricula in self.lista:
            if texto in matricula.periodo or texto in matricula.fecha:
                encontradas.append(matricula)
        return encontradas

    def siguiente(self):
        mayor = 0
        for matricula in self.lista:
            if matricula.id > mayor:
                mayor = matricula.id
        return mayor + 1

    def crear(self, datos):
        # datos = {"estudiante_id": 1, "materia_id": 2, "periodo": "2026-1"}
        error = self.validar(datos)
        if error:
            return False, error
        materia = self.materias.obtener(int(datos["materia_id"]))
        matricula = Matricula(self.siguiente(),
                              int(datos["estudiante_id"]),
                              materia.id,
                              str(datos["periodo"]).strip())
        materia.ocupar_cupo()
        self.materias.guardar()                 # guarda el cupo nuevo en materias.json
        self.lista.append(matricula)
        self.guardar()                          # guarda la matrícula en matriculas.json
        return True, f"Matrícula {matricula.id} registrada en {materia.nombre}"

    def registrar_nota(self, id_matricula, nota):
        matricula = self.obtener(id_matricula)
        if matricula is None:
            return False, f"No existe la matrícula {id_matricula}"
        # es_nota_valida es el método ESTÁTICO de Materia
        if not Materia.es_nota_valida(nota):
            return False, f"Nota inválida: '{nota}' (debe ser un número de 0 a 20)"
        matricula.nota = float(nota)
        self.guardar()
        return True, f"Nota {matricula.nota:.1f} registrada: {matricula.estado()}"

    def actualizar(self, id_matricula, datos):
        # De una matrícula solo se puede cambiar la nota
        if set(datos) != {"nota"}:
            return False, "Solo se puede modificar la nota de una matrícula"
        return self.registrar_nota(id_matricula, datos["nota"])

    def eliminar(self, id_matricula):
        """Retirar una matrícula: se borra y el cupo vuelve a la materia."""
        matricula = self.obtener(id_matricula)
        if matricula is None:
            return False, f"No existe la matrícula {id_matricula}"
        materia = self.materias.obtener(matricula.materia_id)
        if materia is not None:
            materia.liberar_cupo()
            self.materias.guardar()
        self.lista.remove(matricula)
        self.guardar()
        return True, f"Matrícula {id_matricula} retirada y cupo liberado"

    def retirar_matricula(self, id_matricula):
        return self.eliminar(id_matricula)

    # --- propio de matrículas ---
    def certificado(self, id_matricula):
        matricula = self.obtener(id_matricula)
        if matricula is None:
            return None
        # DICCIONARIOS ÍNDICE {id: objeto}: buscar por id sin recorrer nada
        estudiantes = {e.id: e for e in self.estudiantes.leer()}
        materias = {m.id: m for m in self.materias.leer()}
        profesores = {p.id: p for p in self.profesores.leer()}
        estudiante = estudiantes.get(matricula.estudiante_id)
        materia = materias.get(matricula.materia_id)
        nota = f"{matricula.nota:.1f}" if matricula.nota is not None else "sin registrar"
        texto = f"CERTIFICADO #{matricula.id}   periodo: {matricula.periodo}\n"
        if estudiante:
            texto += f"Estudiante: {estudiante.nombre_completo()}   ({estudiante.carnet})\n"
        else:
            texto += "Estudiante: eliminado\n"
        if materia:
            texto += (f"Materia   : {materia.nombre}   ({materia.codigo}) · "
                      f"{materia.creditos} créditos\n")
        else:
            texto += "Materia   : eliminada\n"
        # Profesor de la materia (0 = todavía no se asignó uno)
        if materia and materia.profesor_id == 0:
            texto += "Profesor  : sin asignar\n"
        elif materia:
            profesor = profesores.get(materia.profesor_id)
            if profesor:
                texto += f"Profesor  : {profesor.nombre_completo()}   ({profesor.cedula})\n"
            else:
                texto += "Profesor  : eliminado\n"
        texto += "-" * 42 + "\n"
        texto += f"Nota      : {nota}\n"
        texto += f"Estado    : {matricula.estado()}"
        return texto

    def matriculas_por_estudiante(self):
        """DICCIONARIO de LISTAS: {estudiante_id: [matrículas de ese estudiante]}."""
        agrupadas = {}
        for matricula in self.lista:
            agrupadas.setdefault(matricula.estudiante_id, []).append(matricula)
        return agrupadas

    def promedio_de_estudiante(self, id_estudiante):
        """Promedio de las notas ya registradas, o None si todavía no tiene ninguna."""
        notas = []
        for matricula in self.matriculas_por_estudiante().get(id_estudiante, []):
            if matricula.nota is not None:
                notas.append(matricula.nota)
        if not notas:
            return None
        return round(sum(notas) / len(notas), 2)

    def total_aprobadas(self):
        total = 0
        for matricula in self.lista:
            if matricula.esta_aprobada():
                total += 1
        return totaly