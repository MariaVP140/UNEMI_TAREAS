from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)
from views import (
    SocioController,
    LibroController,
    PrestamoController,
)

# Se crea UN solo controlador de cada tipo y todas las funciones usan esos mismos objetos.
socios = SocioController()
libros = LibroController()
prestamos = PrestamoController(socios, libros)


# =====================================================================
# AYUDAS DE PANTALLA
# =====================================================================
def pausa():
    input("\nPresione Enter para continuar...")


def pedir_entero(etiqueta):
    """Devuelve un entero o None si el usuario escribió otra cosa."""
    try:
        return int(input(etiqueta))
    except ValueError:
        return None


def mostrar_resultado(exito, mensaje):
    # Los controladores devuelven la TUPLA (exito, mensaje)
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)


def mostrar_lista(objetos, vacio="No hay registros todavía."):
    """Sirve para estudiantes, materias y matrículas: cada modelo sabe mostrarse."""
    if not objetos:
        imprimir_info(vacio)
        return
    for objeto in objetos:
        print(f"  {objeto}")
    imprimir_info(f"Total: {len(objetos)}")


def mostrar_detalle(objeto):
    # Recorre el DICCIONARIO del objeto: clave y valor a la vez
    for clave, valor in objeto.a_diccionario().items():
        print(f"  {str(clave).replace('_', ' ').capitalize():<16}: {valor}")


# =====================================================================
# MENÚ DE SOCIOS
# =====================================================================
def crear_socio():
    imprimir_titulo("CREAR SOCIO")
    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "cedula": input("Cédula: "),
        "telefono": input("Teléfono: ")
    }
    mostrar_resultado(*socios.crear(datos))
    pausa()


def listar_socios():
    imprimir_titulo("SOCIOS")
    mostrar_lista(socios.leer(), "Todavía no hay socios.")
    pausa()


def buscar_socio():
    imprimir_titulo("BUSCAR SOCIO")
    termino = input("Nombre, email o cédula: ")
    encontrados = socios.buscar(termino)
    mostrar_lista(encontrados, f"Ninguno coincide con '{termino}'.")
    pausa()


def ver_socio():
    imprimir_titulo("VER SOCIO POR ID")
    socio = socios.obtener(pedir_entero("Id: "))
    if socio is None:
        imprimir_error("No encontrado")
    else:
        mostrar_detalle(socio)
    pausa()


def actualizar_socio():
    imprimir_titulo("ACTUALIZAR SOCIO")
    id_socio = pedir_entero("Id: ")
    socio = socios.obtener(id_socio)
    if socio is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Editando: {socio.etiqueta()}")
    print("Deje en blanco lo que no quiera cambiar.\n")
    cambios = {}
    for campo in ('nombre', 'apellido', 'email', 'cedula', 'telefono'):
        actual = getattr(socio, campo)
        nuevo = input(f"{campo.replace('_', ' ').capitalize()} [{actual}]: ").strip()
        if nuevo:
            cambios[campo] = nuevo
    mostrar_resultado(*socios.actualizar(id_socio, cambios))
    pausa()


def eliminar_socio():
    imprimir_titulo("ELIMINAR SOCIO")
    id_socio = pedir_entero("Id: ")
    socio = socios.obtener(id_socio)
    if socio is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Se eliminará: {socio.etiqueta()}")
    if confirmar("¿Confirma?"):
        mostrar_resultado(*socios.eliminar(id_socio))
    else:
        imprimir_info("Operación cancelada")
    pausa()


# =====================================================================
# MENÚ DE LIBROS
# =====================================================================
def crear_libro():
    imprimir_titulo("CREAR LIBRO")
    datos = {
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "isbn": input("ISBN (10 o 13 dígitos): "),
        "copias": input("Copias: ")
    }
    mostrar_resultado(*libros.crear(datos))
    pausa()


def listar_libros():
    imprimir_titulo("LIBROS")
    mostrar_lista(libros.leer(), "Todavía no hay libros.")
    pausa()


def buscar_libro():
    imprimir_titulo("BUSCAR LIBRO")
    termino = input("Título, autor o ISBN: ")
    encontrados = libros.buscar(termino)
    mostrar_lista(encontrados, f"Ninguno coincide con '{termino}'.")
    pausa()


def ver_libro():
    imprimir_titulo("VER LIBRO POR ID")
    libro = libros.obtener(pedir_entero("Id: "))
    if libro is None:
        imprimir_error("No encontrado")
    else:
        mostrar_detalle(libro)
    pausa()


def actualizar_libro():
    imprimir_titulo("ACTUALIZAR LIBRO")
    id_libro = pedir_entero("Id: ")
    libro = libros.obtener(id_libro)
    if libro is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Editando: {libro.etiqueta()}")
    print("Deje en blanco lo que no quiera cambiar.\n")
    cambios = {}
    for campo in ('titulo', 'autor', 'isbn', 'copias'):
        actual = getattr(libro, campo)
        nuevo = input(f"{campo.replace('_', ' ').capitalize()} [{actual}]: ").strip()
        if nuevo:
            cambios[campo] = nuevo
    mostrar_resultado(*libros.actualizar(id_libro, cambios))
    pausa()


def eliminar_libro():
    imprimir_titulo("ELIMINAR LIBRO")
    id_libro = pedir_entero("Id: ")
    libro = libros.obtener(id_libro)
    if libro is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Se eliminará: {libro.etiqueta()}")
    if confirmar("¿Confirma?"):
        mostrar_resultado(*libros.eliminar(id_libro))
    else:
        imprimir_info("Operación cancelada")
    pausa()


# =====================================================================
# MENÚ DE PRÉSTAMOS
# =====================================================================
def prestar():
    imprimir_titulo("REGISTRAR PRÉSTAMO")
    imprimir_info("Socios:")
    mostrar_lista(socios.leer())
    imprimir_info("Libros:")
    mostrar_lista(libros.leer())
    datos = {
        "socio_id": pedir_entero("\nId del socio: "),
        "libro_id": pedir_entero("Id del libro: "),
    }
    if None in datos.values():
        imprimir_error("Los ids deben ser números enteros")
        return pausa()
    fecha = input("Fecha del préstamo AAAA-MM-DD (Enter = hoy): ").strip()
    if fecha:
        datos["fecha"] = fecha
    mostrar_resultado(*prestamos.crear(datos))
    pausa()


def listar_prestamos():
    imprimir_titulo("PRÉSTAMOS")
    mostrar_lista(prestamos.leer(), "Todavía no hay préstamos.")
    pausa()


def devolver_libro():
    imprimir_titulo("REGISTRAR DEVOLUCIÓN")
    mostrar_lista(prestamos.leer(), "Todavía no hay préstamos.")
    id_prestamo = pedir_entero("\nId del préstamo: ")
    if id_prestamo is None:
        imprimir_error("El id debe ser un número entero")
        return pausa()
    fecha = input("Fecha de devolución AAAA-MM-DD (Enter = hoy): ").strip()
    mostrar_resultado(*prestamos.devolver(id_prestamo, fecha))
    pausa()


def ver_ficha():
    imprimir_titulo("FICHA DEL PRÉSTAMO")
    texto = prestamos.ficha_prestamo(pedir_entero("Id del préstamo: "))
    if texto is None:
        imprimir_error("No existe ese préstamo")
    else:
        print(texto)
    pausa()


def resumen():
    imprimir_titulo("RESUMEN")
    print(f"  Socios      : {len(socios.leer())}")
    print(f"  Libros      : {len(libros.leer())}")
    agotados = libros.sin_copias()
    print(f"  Sin copias  : {', '.join(l.titulo for l in agotados) or 'ninguno'}")
    print(f"  Préstamos   : {len(prestamos.leer())}")
    print(f"  Activos     : {sum(len(v) for v in prestamos.activos_por_socio().values())}")
    print(f"  Atrasados   : {len(prestamos.atrasados())}")
    print(f"  Multas      : ${prestamos.total_multas():.2f}")
    pausa()


# =====================================================================
# MENÚS: DICCIONARIOS tecla -> (texto, función)
# =====================================================================
MENU_SOCIOS = {
    "1": ("Crear socio", crear_socio),
    "2": ("Ver todos", listar_socios),
    "3": ("Buscar", buscar_socio),
    "4": ("Ver por id", ver_socio),
    "5": ("Actualizar", actualizar_socio),
    "6": ("Eliminar", eliminar_socio),
    "0": ("Volver", None),
}

MENU_LIBROS = {
    "1": ("Crear libro", crear_libro),
    "2": ("Ver todos", listar_libros),
    "3": ("Buscar", buscar_libro),
    "4": ("Ver por id", ver_libro),
    "5": ("Actualizar", actualizar_libro),
    "6": ("Eliminar", eliminar_libro),
    "0": ("Volver", None),
}

MENU_PRESTAMOS = {
    "1": ("Registrar préstamo", prestar),
    "2": ("Ver todos", listar_prestamos),
    "3": ("Registrar devolución", devolver_libro),
    "4": ("Ver ficha del préstamo", ver_ficha),
    "0": ("Volver", None),
}


def ejecutar_menu(titulo, opciones):
    """Un solo bucle para los tres submenús."""
    while True:
        imprimir_titulo(titulo)
        for tecla, (texto, _funcion) in opciones.items():
            print(f"  {tecla}. {texto}")
        print()
        tecla = input("Opción: ").strip()
        if tecla not in opciones:               # búsqueda por clave: instantánea
            imprimir_error("Opción no válida")
            pausa()
            continue
        _texto, funcion = opciones[tecla]
        if funcion is None:                      # la opción "Volver"
            break
        funcion()


def main():
    while True:
        imprimir_titulo("SISTEMA DE BIBLIOTECA")
        print("  1. Socios")
        print("  2. Libros")
        print("  3. Préstamos")
        print("  4. Resumen")
        print("  0. Salir\n")
        tecla = input("Opción: ").strip()
        if tecla == "1":
            ejecutar_menu("SOCIOS", MENU_SOCIOS)
        elif tecla == "2":
            ejecutar_menu("LIBROS", MENU_LIBROS)
        elif tecla == "3":
            ejecutar_menu("PRÉSTAMOS", MENU_PRESTAMOS)
        elif tecla == "4":
            resumen()
        elif tecla == "0":
            imprimir_info("¡Hasta luego! 👋")
            break
        else:
            imprimir_error("Opción no válida")
            pausa()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
