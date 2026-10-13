import json  #Permite trabajar con archivos JSON, que sirven para guardar datos de una forma organizada.
import os  # Permite trabajar con carpetas y archivos del sistema operativo. En este código se utiliza, por ejemplo, para comprobar si existe un archivo o una carpeta.


class GestorJSON:   #Lee y guarda una lista de diccionarios en un archivo JSON.
    
    """Lee y guarda datos en un archivo JSON.

    Args:
        ruta: La ubicación y el nombre del archivo JSON que se usará.
    """

    def __init__(self, ruta): #Prepara y guarda la ruta del archivo.
        """Prepara el gestor y crea la carpeta si todavía no existe.

        Args:
            ruta: La ubicación y el nombre del archivo JSON.

        Returns:
            None: Guarda la ruta en el gestor; no devuelve un valor.
        """
        self.ruta = ruta
        carpeta = os.path.dirname(ruta)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

    def leer(self): #Utiliza esa ruta para recuperar los datos guardados.
        """Lee el archivo y devuelve los datos guardados en formato JSON.

        Returns:
            list: Los datos si el archivo contiene una lista; en caso
            contrario, devuelve una lista vacía.
        """
        # Devuelve SIEMPRE una lista: vacía si el archivo no existe o está dañado
        if not os.path.exists(self.ruta):
            return []
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo: # r modo lectora puede ver/leer pero no modificar el archivo
                datos = json.load(archivo) # leer el contenido del archivo y convertirlo de JSON a un objeto Python (lista de diccionarios)
            return datos if isinstance(datos, list) else []
        except (json.JSONDecodeError, OSError):
            # Capturamos errores concretos, nunca un "except:" pelado
            return []

    def guardar(self, datos):
        """Guarda datos en el archivo JSON.

        Args:
            datos: Los datos que se quieren guardar. Deben poder convertirse
                a JSON, por ejemplo, una lista de diccionarios.

        Returns:
            bool: True si se guardaron los datos; False si ocurrió un error.
        """
        try:
            with open(self.ruta, "w", encoding="utf-8") as archivo: # w modo escritura puede escribir y modificar el archivo, si no existe lo crea
                json.dump(datos, archivo, ensure_ascii=False, indent=2)  # convierte los datos Python a un objeto JSON (lista de diccionarios) => formato json
            return True
        except (TypeError, OSError):
            # TypeError aparece si intentas guardar un set: JSON no lo conoce
            return False