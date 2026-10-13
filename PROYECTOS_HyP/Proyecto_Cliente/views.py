from models import Cliente, CAMPOS_CLIENTE
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido

gestor = GestorJSON("data/clientes.json") #crea un objeto que trabajará con el archivo de clientes.

# TUPLAS de configuración: fijas, nadie las modifica en tiempo de ejecución
CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email")
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "telefono", "ciudad")


# ===================== AYUDAS INTERNAS =====================

def emails_registrados(excepto_id=None):
    """Obtiene el conjunto de emails que ya están registrados.

    El conjunto sirve para detectar rápidamente si un email está duplicado.

    Args:
        excepto_id: Id de un cliente que se debe ignorar, por ejemplo,
            al comprobar el email durante una actualización. Por defecto,
            no se ignora ningún cliente.

    Returns:
        set: Emails registrados en minúsculas, excepto el cliente indicado.
    """
    return {
        registro["email"].lower()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def siguiente_id():
    """Calcula el próximo id disponible para un cliente.

    Returns:
        int: El id siguiente al mayor id registrado, o 1 si no hay clientes.
    """
    ids = [registro["id"] for registro in gestor.leer()]
    return max(ids) + 1 if ids else 1 #if ids comprueba si la lista tiene elementos


# ===================== C · CREATE =====================

def crear_cliente(datos):
    """Valida los datos y guarda un cliente nuevo.

    Args:
        datos: Diccionario con los datos del cliente. Debe incluir las claves
            de CAMPOS_CLIENTE; nombre, apellido y email son obligatorios.

    Returns:
        tuple: (éxito, mensaje). Éxito es True si se creó el cliente; si no,
            es False y el mensaje explica el problema.
    """
    try:
        # 1) Normalizo: un diccionario con todos los campos, sin espacios sobrantes
        valores = {campo: str(datos.get(campo, "")).strip() for campo in CAMPOS_CLIENTE}

        # 2) Reviso obligatorios recorriendo la TUPLA
        faltantes = [campo for campo in CAMPOS_OBLIGATORIOS if not valores[campo]]
        if faltantes:
            return False, f"Faltan campos obligatorios: {', '.join(faltantes)}"

        # 3) Formato del email
        if not es_email_valido(valores["email"]):
            return False, f"El email '{valores['email']}' no tiene un formato válido"

        # 4) Duplicado: búsqueda instantánea dentro del CONJUNTO
        if valores["email"].lower() in emails_registrados():
            return False, "Ese email ya está registrado"

        # 5) Creo el objeto del Modelo. ** convierte el diccionario en argumentos
        cliente = Cliente(siguiente_id(), **valores)

        # 6) Agrego a la LISTA y guardo
        registros = gestor.leer()
        registros.append(cliente.a_diccionario())
        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"

        return True, f"Cliente {cliente.obtener_nombre_completo()} creado con id {cliente.id}"

    except Exception as error:
        return False, f"Error inesperado: {error}"


# ===================== R · READ =====================

def obtener_todos():
    """Lee y devuelve todos los clientes guardados.

    Returns:
        list: Lista de objetos Cliente. Si no hay clientes, devuelve una
            lista vacía.
    """
    return [Cliente.desde_diccionario(registro) for registro in gestor.leer()]


def obtener_por_id(id_cliente): 
    """Busca un cliente usando su id.

    Args:
        id_cliente: Id del cliente que se quiere encontrar.

    Returns:
        Cliente | None: El cliente encontrado, o None si no existe ese id.
    """
    for cliente in obtener_todos():
        if cliente.id == id_cliente:
            return cliente
    return None


# ===================== S · SEARCH =====================

def buscar_clientes(termino):
    """Busca clientes que contengan el término en sus campos buscables.

    La búsqueda es lineal: revisa cada cliente y los campos indicados en
    CAMPOS_BUSCABLES.

    Args:
        termino: Texto que se buscará en los datos de cada cliente.

    Returns:
        list: Clientes que coinciden. Si el término está vacío o no hay
            coincidencias, devuelve una lista vacía.
    """
    termino = termino.strip().lower()
    if not termino:
        return []

    encontrados = []
    for registro in gestor.leer():
        for campo in CAMPOS_BUSCABLES:                 # recorro la TUPLA de campos
            if termino in str(registro.get(campo, "")).lower():
                encontrados.append(Cliente.desde_diccionario(registro))
                break                                   # ya coincidió: paso al siguiente cliente
    return encontrados


# ===================== U · UPDATE =====================

def actualizar_cliente(id_cliente, cambios):
    """Valida y guarda cambios en un cliente existente.

    Args:
        id_cliente: Id del cliente que se quiere actualizar.
        cambios: Diccionario con solo los campos que se quieren modificar.

    Returns:
        tuple: (éxito, mensaje). Éxito es True si se actualizó el cliente;
            si no, es False y el mensaje explica el problema.
    """
    try:
        # DIFERENCIA DE CONJUNTOS: ¿mandaron algún campo que no existe?
        desconocidos = set(cambios) - set(CAMPOS_CLIENTE)
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        if not cambios:
            return False, "No se indicó ningún cambio"

        if "email" in cambios:
            if not es_email_valido(cambios["email"]):
                return False, "El email no tiene un formato válido"
            if cambios["email"].lower() in emails_registrados(excepto_id=id_cliente):
                return False, "Ese email ya lo usa otro cliente"

        registros = gestor.leer()
        posicion = None
        for indice, registro in enumerate(registros):   # enumerate me da índice y valor
            if registro["id"] == id_cliente:
                posicion = indice
                break

        if posicion is None:
            return False, f"No existe un cliente con id {id_cliente}"

        registros[posicion].update(cambios)             # actualizo el diccionario en su lugar
        gestor.guardar(registros) # actualiza el archivo con la LISTA modificada
        return True, f"Cliente {id_cliente} actualizado ({len(cambios)} campo/s)"

    except Exception as error: # "Captura el error y guárdalo en una variable llamada error."
        return False, f"Error inesperado: {error}"


# ===================== D · DELETE =====================

def eliminar_cliente(id_cliente):
    """Elimina un cliente usando su id.

    Args:
        id_cliente: Id del cliente que se quiere eliminar.

    Returns:
        tuple: (éxito, mensaje). Éxito es True si se eliminó el cliente;
            si no, es False y el mensaje indica que no se encontró.
    """
    registros = gestor.leer()
    # Construyo una LISTA NUEVA sin ese registro: nunca borro mientras recorro
    quedan = [registro for registro in registros if registro["id"] != id_cliente]

    if len(quedan) == len(registros):
        return False, f"No existe un cliente con id {id_cliente}"


    gestor.guardar(quedan)
    return True, f"Cliente {id_cliente} eliminado"


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