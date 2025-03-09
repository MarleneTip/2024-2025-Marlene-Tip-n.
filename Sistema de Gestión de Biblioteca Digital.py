class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (ISBN: {self.isbn}) - Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id  # ID único
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = {}  # Diccionario {ID: Usuario}

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("ID de usuario ya registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)  # Elimina el libro del diccionario de disponibles
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Devuelve el libro a la biblioteca
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = [libro for libro in self.libros.values()
                      if (titulo is None or libro.info[0] == titulo)
                      and (autor is None or libro.info[1] == autor)
                      and (categoria is None or libro.categoria == categoria)]

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con esos criterios.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("Este usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas
biblio = Biblioteca()
libro1 = Libro("1984", "George Orwell", "Ficción", "123456")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "789012")
usuario1 = Usuario("Juan Pérez", "U001")

biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.registrar_usuario(usuario1)
biblio.prestar_libro("U001", "123456")
biblio.listar_libros_prestados("U001")
biblio.devolver_libro("U001", "123456")
biblio.buscar_libro(autor="Gabriel García Márquez")
