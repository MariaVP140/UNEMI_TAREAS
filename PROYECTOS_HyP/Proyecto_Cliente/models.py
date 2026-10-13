import json

# TUPLA de campos: el orden y los nombres son fijos, por eso no es una lista.
# La usan el Controlador y la Vista para no repetir textos sueltos.
CAMPOS_CLIENTE = ("nombre", "apellido", "email", "telefono", "ciudad", "direccion")


class Cliente:
    """MODELO: representa a un cliente."""

    def __init__(self, id_cliente, nombre, apellido, email, telefono, ciudad, direccion):
        """Crea un cliente con sus datos personales.

        Args:
            id_cliente: Identificador único del cliente.
            nombre: Nombre del cliente.
            apellido: Apellido del cliente.
            email: Correo electrónico del cliente.
            telefono: Número de teléfono del cliente.
            ciudad: Ciudad donde vive el cliente.
            direccion: Dirección del cliente.

        Returns:
            None: Guarda los datos en el objeto; no devuelve un valor.
        """
        self.id = id_cliente          # no usamos 'id' como parámetro: es una función de Python
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.direccion = direccion

    def obtener_nombre_completo(self):
        """Une el nombre y el apellido del cliente.

        Returns:
            str: El nombre completo del cliente.
        """
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        """Convierte los datos del cliente en un diccionario.

        Returns:
            dict: Los datos del cliente, listos para guardarse como JSON.
        """
        # Objeto -> diccionario (listo para JSON)
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "ciudad": self.ciudad,
            "direccion": self.direccion,
        }

    @classmethod #Es un decorador que indica que el método pertenece a la clase y
    # recibe la propia clase como primer parámetro, en lugar de recibir un objeto mediante self.
    def desde_diccionario(cls, datos):
        """Crea un cliente usando los datos de un diccionario.

        Args:
            datos: Diccionario con los datos del cliente, incluido su id.

        Returns:
            Cliente: Un nuevo objeto Cliente con los datos recibidos.
        """
        # Diccionario -> objeto. Es un método de la CLASE, no de un objeto:
        # se usa así -> Cliente.desde_diccionario({...})
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["telefono"],
            datos.get("ciudad", ""),      # .get por si el archivo es de una versión vieja
            datos.get("direccion", ""),
        )

    def a_json(self): #combierte el diccionario a una cadena de texto con formato JSON 
        """Convierte los datos del cliente en una cadena JSON.

        Returns:
            str: Los datos del cliente escritos en formato JSON.
        """
        return json.dumps(self.a_diccionario(), ensure_ascii=False)

    def __str__(self): #Define cómo se muestra el objeto cuando usamos print().
        # Es un método especial de Python que determina, cómo se representa un objeto cuando lo mostramos como texto.

        """Prepara una versión breve del cliente para mostrar como texto.

        Returns:
            str: El id, el nombre completo y el correo del cliente.
        """
        return f"[{self.id}] {self.obtener_nombre_completo()} - {self.email}"


class Estudiante:
    """MODELO: representa a un estudiante. Usa las cuatro colecciones."""

    def __init__(self, id_estudiante, nombre, apellido, email, carnet, notas=None, materias=None):
        """Crea un estudiante y prepara sus notas y materias.

        Args:
            id_estudiante: Identificador único del estudiante.
            nombre: Nombre del estudiante.
            apellido: Apellido del estudiante.
            email: Correo electrónico del estudiante.
            carnet: Código de matrícula del estudiante.
            notas: Diccionario con las materias y sus listas de notas.
                Si no se recibe, se empieza con un diccionario vacío.
            materias: Materias en las que está inscrito. Si no se recibe,
                se empieza con un conjunto vacío.

        Returns:
            None: Guarda los datos en el objeto; no devuelve un valor.
        """
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet                      # ej: EST2026001
        # DICCIONARIO DE LISTAS: {"Matemática": [18, 19], "Inglés": [17]}
        self.notas = notas if notas else {}
        # CONJUNTO: materias en las que está inscrito, sin repetidos
        self.materias = set(materias) if materias else set()

    def obtener_nombre_completo(self):
        """Une el nombre y el apellido del estudiante.

        Returns:
            str: El nombre completo del estudiante.
        """
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        """Inscribe al estudiante en una materia.

        Args:
            materia: Nombre de la materia en la que se inscribirá.

        Returns:
            None: Actualiza el conjunto de materias del estudiante.
        """
        # add() no duplica: si ya estaba inscrito, no pasa nada
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        """Agrega una nota y, si hace falta, inscribe al estudiante en la materia.

        Args:
            materia: Nombre de la materia asociada a la nota.
            nota: Calificación que se agregará a la lista de notas.

        Returns:
            None: Actualiza las materias y las notas del estudiante.
        """
        self.inscribir_materia(materia)
        # setdefault crea la lista vacía la primera vez que aparece la materia
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        """Calcula el promedio de todas las notas del estudiante.

        Returns:
            int | float: El promedio redondeado a dos decimales, o 0 si todavía
            no hay notas.
        """
        todas = []
        for lista_notas in self.notas.values():
            todas.extend(lista_notas)
        if not todas:
            return 0
        return round(sum(todas) / len(todas), 2)

    def materias_en_comun(self, otro_estudiante):
        """Busca las materias que comparte con otro estudiante.

        Args:
            otro_estudiante: El estudiante con quien se compararán las materias.

        Returns:
            set: Las materias que tienen inscritas ambos estudiantes.
        """
        # INTERSECCIÓN de conjuntos: qué materias comparten dos estudiantes
        return self.materias & otro_estudiante.materias

    def a_diccionario(self):
        """Convierte los datos del estudiante en un diccionario.

        Returns:
            dict: Los datos del estudiante, con las materias como una lista,
            listos para guardarse como JSON.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,
            # JSON no sabe guardar un set: lo convertimos a lista ordenada
            "materias": sorted(self.materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un estudiante usando los datos de un diccionario.

        Args:
            datos: Diccionario con los datos del estudiante.

        Returns:
            Estudiante: Un nuevo objeto Estudiante con los datos recibidos.
        """
        return cls(
            datos["id"], datos["nombre"], datos["apellido"], datos["email"],
            datos["carnet"],
            notas=datos.get("notas", {}),
            # y al leer lo volvemos a convertir en set
            materias=set(datos.get("materias", [])),
        )

    def __str__(self):
        """Prepara una versión breve del estudiante para mostrar como texto.

        Returns:
            str: El carnet, el nombre completo y el promedio del estudiante.
        """
        return f"[{self.carnet}] {self.obtener_nombre_completo()} - Promedio: {self.obtener_promedio()}"