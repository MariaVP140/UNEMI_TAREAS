import os

# DICCIONARIO: cada color tiene su etiqueta y su código de consola
COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

# TUPLA: respuestas afirmativas aceptadas. Es fija, por eso no es lista.
RESPUESTAS_SI = ("si", "sí", "s", "yes", "y")


def limpiar_pantalla():
    """ Borra todo lo que hay escrito en la consola .
        
        funciona en Windows (usa "cls") y en Linux/Mac (usa "clear)
        
        Arg:
            No recibe nada.
              
        Return: 
            None: NO devuelve nada, solo limpia la pantalla.
               
               Ejemplo:
                  >>> limpiar_pantalla()
    """
    # os.name vale "posix" en Linux/Mac y "nt" en Windows
    # -En Linux/Mac el comando para limpiar es "clear".
    # -En Windows el comando es "cls".
    # os.system(...) ejecuta ese comando como si lo escribieras tú.
    
        
    os.system("clear" if os.name == "posix" else "cls")


def imprimir_color(texto, color):
    """Imprime un texto con el color indicado.

    Args:
        texto: El mensaje que se mostrará en la consola.
        color: El nombre de un color de COLORES, por ejemplo "ROJO".
            Si el nombre no existe, se usa el color blanco.

    Returns:
        None: Solo imprime el texto; no devuelve un valor.
    """
    codigo = COLORES.get(color, COLORES["BLANCO"])   # .get evita el error si el color no existe
    print(f"{codigo}{texto}{COLORES['RESET']}")


def imprimir_titulo(texto):
    """Limpia la consola e imprime un título en azul.

    Args:
        texto: El título que se mostrará.

    Returns:
        None: Solo modifica lo que aparece en la consola.
    """
    limpiar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"  {texto}".center(60))
    imprimir_color("=" * 60, "AZUL")
    print()


def imprimir_exito(mensaje):
    """Imprime un mensaje de éxito en verde.

    Args:
        mensaje: El texto que se mostrará como mensaje de éxito.

    Returns:
        None: Solo imprime el mensaje; no devuelve un valor.
    """
    imprimir_color(f"✓ {mensaje}", "VERDE")


def imprimir_error(mensaje):
    """Imprime un mensaje de error en rojo.

    Args:
        mensaje: El texto que se mostrará como mensaje de error.

    Returns:
        None: Solo imprime el mensaje; no devuelve un valor.
    """
    imprimir_color(f"✗ {mensaje}", "ROJO")


def imprimir_info(mensaje):
    """Imprime un mensaje informativo en cian.

    Args:
        mensaje: El texto informativo que se mostrará.

    Returns:
        None: Solo imprime el mensaje; no devuelve un valor.
    """
    imprimir_color(f"ℹ {mensaje}", "CYAN")


def confirmar(pregunta):
    """Pregunta algo y comprueba si la respuesta es afirmativa.

    Args:
        pregunta: La pregunta que se mostrará antes de pedir la respuesta.

    Returns:
        bool: True si la respuesta está en RESPUESTAS_SI; False en otro caso.
    """
    # Devuelve True si el usuario respondió algo de la tupla RESPUESTAS_SI
    respuesta = input(f"{pregunta} (si/no): ").strip().lower()
    return respuesta in RESPUESTAS_SI


def es_email_valido(texto):
    """Comprueba de forma básica si un texto parece una dirección de email.

    Args:
        texto: El texto que se quiere comprobar.

    Returns:
        bool: True si tiene un formato básico válido; False si no lo tiene.
    """
    # Validación mínima: un @, algo antes, algo después y un punto al final
    texto = texto.strip()
    if texto.count("@") != 1:
        return False
    usuario, dominio = texto.split("@")
    return len(usuario) > 0 and "." in dominio and not dominio.endswith(".")


if __name__ == "__main__":
    # Este bloque corre solo al ejecutar este archivo directamente.
    limpiar_pantalla()

    # Probamos las funciones que muestran texto y colores.
    imprimir_titulo("Prueba de herramientas")
    imprimir_color("Texto de prueba", "AZUL")
    imprimir_color("Color desconocido: se usa blanco", "MORADO")
    imprimir_exito("Mensaje de exito")
    imprimir_error("Mensaje de error")
    imprimir_info("Mensaje informativo")

    # confirmar() pide una respuesta y devuelve True o False.
    if confirmar("¿Quieres continuar?"):
        imprimir_exito("Respondiste que si")
    else:
        imprimir_info("Respondiste que no")

    # Probamos es_email_valido() con un correo correcto y uno incorrecto.
    print()
    print("--- Prueba de correos ---")
    correos = ["persona@ejemplo.com", "correo-sin-arroba"]

    for correo in correos:
        resultado = es_email_valido(correo)
        print(f"{correo} -> {resultado}")