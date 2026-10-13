from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)
from views import (
    HuespedController,
    HabitacionController,
    ReservaController,
)

# Se crea UN solo controlador de cada tipo y todas las funciones usan esos mismos objetos.
huespedes = HuespedController()
habitaciones = HabitacionController()
reservas = ReservaController(huespedes, habitaciones)


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
# MENÚ DE HUÉSPEDES
# =====================================================================
def crear_huesped():
    imprimir_titulo("CREAR HUÉSPED")
    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "cedula": input("Cédula: "),
        "telefono": input("Teléfono: ")
    }
    mostrar_resultado(*huespedes.crear(datos))
    pausa()


def listar_huespedes():
    imprimir_titulo("HUÉSPEDES")
    mostrar_lista(huespedes.leer(), "Todavía no hay huéspedes.")
    pausa()


def buscar_huesped():
    imprimir_titulo("BUSCAR HUÉSPED")
    termino = input("Nombre, email o cédula: ")
    encontrados = huespedes.buscar(termino)
    mostrar_lista(encontrados, f"Ninguno coincide con '{termino}'.")
    pausa()


def ver_huesped():
    imprimir_titulo("VER HUÉSPED POR ID")
    huesped = huespedes.obtener(pedir_entero("Id: "))
    if huesped is None:
        imprimir_error("No encontrado")
    else:
        mostrar_detalle(huesped)
    pausa()


def actualizar_huesped():
    imprimir_titulo("ACTUALIZAR HUÉSPED")
    id_huesped = pedir_entero("Id: ")
    huesped = huespedes.obtener(id_huesped)
    if huesped is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Editando: {huesped.etiqueta()}")
    print("Deje en blanco lo que no quiera cambiar.\n")
    cambios = {}
    for campo in ('nombre', 'apellido', 'email', 'cedula', 'telefono'):
        actual = getattr(huesped, campo)
        nuevo = input(f"{campo.replace('_', ' ').capitalize()} [{actual}]: ").strip()
        if nuevo:
            cambios[campo] = nuevo
    mostrar_resultado(*huespedes.actualizar(id_huesped, cambios))
    pausa()


def eliminar_huesped():
    imprimir_titulo("ELIMINAR HUÉSPED")
    id_huesped = pedir_entero("Id: ")
    huesped = huespedes.obtener(id_huesped)
    if huesped is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Se eliminará: {huesped.etiqueta()}")
    if confirmar("¿Confirma?"):
        mostrar_resultado(*huespedes.eliminar(id_huesped))
    else:
        imprimir_info("Operación cancelada")
    pausa()


# =====================================================================
# MENÚ DE HABITACIONES
# =====================================================================
def crear_habitacion():
    imprimir_titulo("CREAR HABITACIÓN")
    datos = {
        "numero": input("Número (ej. 101): "),
        "tipo": input("Tipo (Simple, Doble o Suite): "),
        "precio_noche": input("Precio por noche: ")
    }
    mostrar_resultado(*habitaciones.crear(datos))
    pausa()


def listar_habitaciones():
    imprimir_titulo("HABITACIONES")
    mostrar_lista(habitaciones.leer(), "Todavía no hay habitaciones.")
    pausa()


def buscar_habitacion():
    imprimir_titulo("BUSCAR HABITACIÓN")
    termino = input("Número o tipo: ")
    encontrados = habitaciones.buscar(termino)
    mostrar_lista(encontrados, f"Ninguno coincide con '{termino}'.")
    pausa()


def ver_habitacion():
    imprimir_titulo("VER HABITACIÓN POR ID")
    habitacion = habitaciones.obtener(pedir_entero("Id: "))
    if habitacion is None:
        imprimir_error("No encontrado")
    else:
        mostrar_detalle(habitacion)
    pausa()


def actualizar_habitacion():
    imprimir_titulo("ACTUALIZAR HABITACIÓN")
    id_habitacion = pedir_entero("Id: ")
    habitacion = habitaciones.obtener(id_habitacion)
    if habitacion is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Editando: {habitacion.etiqueta()}")
    print("Deje en blanco lo que no quiera cambiar.\n")
    cambios = {}
    for campo in ('numero', 'tipo', 'precio_noche'):
        actual = getattr(habitacion, campo)
        nuevo = input(f"{campo.replace('_', ' ').capitalize()} [{actual}]: ").strip()
        if nuevo:
            cambios[campo] = nuevo
    mostrar_resultado(*habitaciones.actualizar(id_habitacion, cambios))
    pausa()


def eliminar_habitacion():
    imprimir_titulo("ELIMINAR HABITACIÓN")
    id_habitacion = pedir_entero("Id: ")
    habitacion = habitaciones.obtener(id_habitacion)
    if habitacion is None:
        imprimir_error("No encontrado")
        return pausa()
    imprimir_info(f"Se eliminará: {habitacion.etiqueta()}")
    if confirmar("¿Confirma?"):
        mostrar_resultado(*habitaciones.eliminar(id_habitacion))
    else:
        imprimir_info("Operación cancelada")
    pausa()


# =====================================================================
# MENÚ DE RESERVAS
# =====================================================================
def reservar():
    imprimir_titulo("HACER RESERVA")
    imprimir_info("Huéspedes:")
    mostrar_lista(huespedes.leer())
    imprimir_info("Habitaciones:")
    mostrar_lista(habitaciones.leer())
    datos = {
        "huesped_id": pedir_entero("\nId del huésped: "),
        "habitacion_id": pedir_entero("Id de la habitación: "),
    }
    if None in datos.values():
        imprimir_error("Los ids deben ser números enteros")
        return pausa()
    datos["entrada"] = input("Entrada AAAA-MM-DD: ")
    datos["salida"] = input("Salida AAAA-MM-DD: ")
    mostrar_resultado(*reservas.crear(datos))
    pausa()


def listar_reservas():
    imprimir_titulo("RESERVAS")
    mostrar_lista(reservas.leer(), "Todavía no hay reservas.")
    pausa()


def cancelar_reserva():
    imprimir_titulo("CANCELAR RESERVA")
    id_reserva = pedir_entero("Id de la reserva: ")
    if id_reserva and confirmar("Se liberarán las fechas. ¿Confirma?"):
        mostrar_resultado(*reservas.eliminar(id_reserva))
    else:
        imprimir_info("Operación cancelada")
    pausa()


def ver_comprobante():
    imprimir_titulo("COMPROBANTE DE RESERVA")
    texto = reservas.comprobante(pedir_entero("Id de la reserva: "))
    if texto is None:
        imprimir_error("No existe esa reserva")
    else:
        print(texto)
    pausa()


def buscar_libres():
    imprimir_titulo("HABITACIONES LIBRES")
    entrada = input("Entrada AAAA-MM-DD: ")
    salida = input("Salida AAAA-MM-DD: ")
    libres = reservas.habitaciones_libres(entrada, salida)
    if libres is None:
        imprimir_error("Fechas inválidas: use AAAA-MM-DD y que la salida sea posterior a la entrada")
    else:
        mostrar_lista(libres, "No hay habitaciones libres en ese rango.")
    pausa()


def resumen():
    imprimir_titulo("RESUMEN")
    print(f"  Huéspedes      : {len(huespedes.leer())}")
    print(f"  Habitaciones   : {len(habitaciones.leer())}")
    print(f"  Reservas       : {len(reservas.leer())}")
    print(f"  Activas        : {reservas.total_activas()}")
    print(f"  Ingresos activos: ${reservas.ingresos_esperados():.2f}")
    pausa()


# =====================================================================
# MENÚS: DICCIONARIOS tecla -> (texto, función)
# =====================================================================
MENU_HUESPEDES = {
    "1": ("Crear huésped", crear_huesped),
    "2": ("Ver todos", listar_huespedes),
    "3": ("Buscar", buscar_huesped),
    "4": ("Ver por id", ver_huesped),
    "5": ("Actualizar", actualizar_huesped),
    "6": ("Eliminar", eliminar_huesped),
    "0": ("Volver", None),
}

MENU_HABITACIONES = {
    "1": ("Crear habitación", crear_habitacion),
    "2": ("Ver todas", listar_habitaciones),
    "3": ("Buscar", buscar_habitacion),
    "4": ("Ver por id", ver_habitacion),
    "5": ("Actualizar", actualizar_habitacion),
    "6": ("Eliminar", eliminar_habitacion),
    "0": ("Volver", None),
}

MENU_RESERVAS = {
    "1": ("Hacer reserva", reservar),
    "2": ("Ver todas", listar_reservas),
    "3": ("Cancelar reserva", cancelar_reserva),
    "4": ("Ver comprobante", ver_comprobante),
    "5": ("Buscar habitaciones libres", buscar_libres),
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
        imprimir_titulo("SISTEMA DE HOTEL")
        print("  1. Huéspedes")
        print("  2. Habitaciones")
        print("  3. Reservas")
        print("  4. Resumen")
        print("  0. Salir\n")
        tecla = input("Opción: ").strip()
        if tecla == "1":
            ejecutar_menu("HUÉSPEDES", MENU_HUESPEDES)
        elif tecla == "2":
            ejecutar_menu("HABITACIONES", MENU_HABITACIONES)
        elif tecla == "3":
            ejecutar_menu("RESERVAS", MENU_RESERVAS)
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
