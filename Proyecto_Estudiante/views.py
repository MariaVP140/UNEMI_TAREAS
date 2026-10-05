from models import Estudiante,CAMPOS_ESTUDIANTE
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido

gestor = GestorJSON("data/estudiantes.json") #crea un objeto que trabajará con el archivo de clientes.

# TUPLAS de configuración: fijas, nadie las modifica en tiempo de ejecución
CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email", "carnet")
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "carnet")

# ===================== AYUDAS INTERNAS ====================== 


def carnet_registrados(excepto_id=None):
    """Obtiene el conjunto de carnets que ya están registrados.

    El conjunto sirve para detectar rápidamente si un carnet está duplicado.

    Returns:
        set: Carnets registrados en minúsculas.
    """
    return {
        registro["carnet"].lower()
        for registro in gestor.leer()
    }


def siguiente_id():
    """Calcula el próximo id disponible para un cliente.

    Returns:
        int: El id siguiente al mayor id registrado, o 1 si no hay clientes.
    """
    ids = [registro["id"] for registro in gestor.leer()]
    return max(ids) + 1 if ids else 1 #if ids comprueba si la lista tiene elementos


# ===================== C · CREATE =====================

def crear_estudiante(datos):
    """Valida los datos y guarda un estudiante nuevo.

    Args:
        datos: Diccionario con los datos del estudiante. Debe incluir las claves
            de CAMPOS_ESTUDIANTE; nombre, apellido y email son obligatorios.

    Returns:
        tuple: (éxito, mensaje). Éxito es True si se creó el estudiante; si no,
            es False y el mensaje explica el problema.
    """
    try:
        # 1) Normalizo: un diccionario con todos los campos, sin espacios sobrantes
        valores = {campo: str(datos.get(campo, "")).strip() for campo in CAMPOS_ESTUDIANTE}

        # 2) Reviso obligatorios recorriendo la TUPLA
        faltantes = [campo for campo in CAMPOS_OBLIGATORIOS if not valores[campo]]
        if faltantes:
            return False, f"Faltan campos obligatorios: {', '.join(faltantes)}"

        # 3) Formato del email
        if not es_email_valido(valores["email"]):
            return False, f"El email '{valores['email']}' no tiene un formato válido"

        # 4) Duplicado: búsqueda instantánea dentro del CONJUNTO
        if valores["carnet"].lower() in carnet_registrados():
            return False, "Ese carnet ya está registrado"

        # 5) Creo el objeto del Modelo. ** convierte el diccionario en argumentos
        estudiante= Estudiante(siguiente_id(), **valores)

        # 6) Agrego a la LISTA y guardo
        registros = gestor.leer()
        registros.append(estudiante.a_diccionario())
        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"

        return True, f"Estudiante {estudiante.obtener_nombre_completo()} creado con id {estudiante.id}"

    except Exception as error:
        return False, f"Error inesperado: {error}"


# ===================== R · READ =====================

def obtener_todos():
    """Lee y devuelve todos los estudiantes guardados.

    Returns:
        list: Lista de objetos Estudiante. Si no hay estudiantes, devuelve una
            lista vacía.
    """
    return [Estudiante.desde_diccionario(registro) for registro in gestor.leer()]


def obtener_por_id(id_estudiante):
    """Busca un estudiante usando su id.

    Args:
        id_estudiante: Id del estudiante que se quiere encontrar.

    Returns:
        Estudiante | None: El estudiante encontrado, o None si no existe ese id.
    """
    for estudiante in obtener_todos():
        if estudiante.id == id_estudiante:
            return estudiante
    return None


# ===================== S · SEARCH =====================

def buscar_estudiantes(termino):
    """Busca estudiantes que contengan el término en sus campos buscables.

    La búsqueda es lineal: revisa cada estudiante y los campos indicados en
    CAMPOS_BUSCABLES.

    Args:
        termino: Texto que se buscará en los datos de cada estudiante.

    Returns:
        list: Estudiantes que coinciden. Si el término está vacío o no hay
            coincidencias, devuelve una lista vacía.
    """
    termino = termino.strip().lower()
    if not termino:
        return []

    encontrados = []
    for registro in gestor.leer():
        for campo in CAMPOS_BUSCABLES:                 # recorro la TUPLA de campos
            if termino in str(registro.get(campo, "")).lower():
                encontrados.append(Estudiante.desde_diccionario(registro))
                break                                   # ya coincidió: paso al siguiente cliente
    return encontrados


# ===================== U · UPDATE =====================

def actualizar_estudiante(id_estudiante, cambios):
    """Valida y guarda cambios en un estudiante existente.

    Args:
        id_estudiante: Id del estudiante que se quiere actualizar.
        cambios: Diccionario con solo los campos que se quieren modificar.

    Returns:
        tuple: (éxito, mensaje). Éxito es True si se actualizó el estudiante;
            si no, es False y el mensaje explica el problema.
    """
    try:
        # DIFERENCIA DE CONJUNTOS: ¿mandaron algún campo que no existe?
        desconocidos = set(cambios) - set(CAMPOS_ESTUDIANTE)
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        if not cambios:
            return False, "No se indicó ningún cambio"

        if "carnet" in cambios:
            if not es_email_valido(cambios["email"]):
                return False, "El carnet no tiene un formato válido"
            if cambios["carnet"].lower() in carnet_registrados(excepto_id=id_estudiante):
                return False, "Ese carnet ya lo usa otro estudiante"

        registros = gestor.leer()
        posicion = None
        for indice, registro in enumerate(registros):   # enumerate me da índice y valor
            if registro["id"] == id_estudiante:
                posicion = indice
                break

        if posicion is None:
            return False, f"No existe un cliente con id {id_estudiante}"

        registros[posicion].update(cambios)             # actualizo el diccionario en su lugar
        gestor.guardar(registros) # actualiza el archivo con la LISTA modificada
        return True, f"Estudiante {id_estudiante} actualizado ({len(cambios)} campo/s)"

    except Exception as error: # "Captura el error y guárdalo en una variable llamada error."
        return False, f"Error inesperado: {error}"


# ===================== D · DELETE =====================

def eliminar_estudiante(id_estudiante):
    """Elimina un estudiante usando su id.

    Args:
        id_estudiante: Id del estudiante que se quiere eliminar.

    Returns:
        tuple: (éxito, mensaje). Éxito es True si se eliminó el estudiante;
            si no, es False y el mensaje indica que no se encontró.
    """
    registros = gestor.leer()
    # Construyo una LISTA NUEVA sin ese registro: nunca borro mientras recorro
    quedan = [registro for registro in registros if registro["id"] != id_estudiante]

    if len(quedan) == len(registros):
        return False, f"No existe un estudiante con id {id_estudiante}"


    gestor.guardar(quedan)
    return True, f"Estudiante {id_estudiante} eliminado"

# ===================== notas =====================

def agregar_nota(id_estudiante,materia,nota):
    """Agrega una nota a un estudiante específico.
    Args:
        id_estudiante: Id del estudiante al que se le agregará la nota.
        materia: Nombre de la materia.
        nota: Valor de la nota.

    returns:
        tuple: (éxito, mensaje). Éxito es True si se agregó la nota;
            si no, es False y el mensaje indica que no se encontró.
   """

    try:
        if nota < 0 or nota > 20:
            return False, "La nota debe estar entre 0 y 20"

        estudiante = obtener_por_id(id_estudiante)

        if estudiante is None:
            return False, f"No existe un estudiante con id {id_estudiante}"

        estudiante.agregar_nota(materia, nota)

        registros = gestor.leer()

        for indice, registro in enumerate(registros):
            if registro["id"] == id_estudiante:
                registros[indice] = estudiante.a_diccionario()
                break

        if not gestor.guardar(registros):
            return False, "No se pudo guardar la nota"

        return True, f"Nota agregada correctamente a {estudiante.obtener_nombre_completo()}"

    except Exception as error:
        return False, f"Error inesperado: {error}"



def materias_ofertadas():
    """Obtiene el conjunto de materias en las que hay al menos un estudiante inscrito.
    Returns:
        set: Conjunto de nombres de materias.
    """
    materias = set()

    for estudiante in obtener_todos():
        materias.update(estudiante.materias)

    return materias


def estudiantes_en_comun(id_a, id_b):
    """Encuentra las materias que comparten dos estudiantes.
    Args:
        id_a: Id del primer estudiante.
        id_b: Id del segundo estudiante.

    Returns:
        tuple: (éxito, materias). Éxito es True si ambos estudiantes existen;
            si no, es False y materias es una lista vacía.
    """
    estudiante_a = obtener_por_id(id_a)
    estudiante_b = obtener_por_id(id_b)

    if estudiante_a is None:
        return False, f"No existe un estudiante con id {id_a}"

    if estudiante_b is None:
        return False, f"No existe un estudiante con id {id_b}"

    return True, estudiante_a.materias_en_comun(estudiante_b)


# ===================== EXTRA: estadísticas con conjuntos =====================

def estadisticas():
    """Calcula un resumen de los clientes registrados.

    El resumen incluye el total de clientes, las ciudades, los dominios de
    sus emails y los clientes que no tienen teléfono.

    Returns:
        dict: Diccionario con las claves "total", "ciudades", "dominios"
            y "sin_telefono".
    """
    registros = gestor.leer()
    ciudades = {r.get("ciudad", "").title() for r in registros if r.get("ciudad")}
    dominios = {r["email"].split("@")[1].lower() for r in registros if "@" in r["email"]}
    sin_telefono = [r["nombre"] for r in registros if not r.get("telefono")]

    return {
        "total": len(registros),
        "ciudades": sorted(ciudades),
        "dominios": sorted(dominios),
        "sin_telefono": sin_telefono,
    }