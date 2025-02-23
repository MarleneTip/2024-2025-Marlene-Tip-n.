import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def to_string(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(producto_str):
        id_producto, nombre, cantidad, precio = producto_str.strip().split(",")
        return Producto(id_producto, nombre, int(cantidad), float(precio))


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                for producto in self.productos:
                    archivo.write(producto.to_string() + "\n")
        except PermissionError:
            print("Error: No se tienen permisos para modificar el archivo.")
        except Exception as e:
            print(f"Error desconocido al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            return
        try:
            with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                for linea in archivo:
                    self.productos.append(Producto.from_string(linea))
        except FileNotFoundError:
            print("Error: No se encontró el archivo de inventario.")
        except Exception as e:
            print(f"Error desconocido al cargar el inventario: {e}")

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El producto con este ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido correctamente y guardado en el archivo.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print(f"Producto con ID {id_producto} eliminado y cambios guardados.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print(f"Producto con ID {id_producto} actualizado y guardado en archivo.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            print("Productos encontrados:")
            for p in productos_encontrados:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        print("Productos en el inventario:")
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")


def menu():
    inventario = Inventario()
    while True:
        print("\n=== Sistema de Gestión de Inventarios ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            id_producto = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            precio = float(input("Introduce el precio del producto: "))
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(nuevo_producto)

        elif opcion == "2":
            id_producto = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Introduce el ID del producto a actualizar: ")
            print("Deja en blanco si no deseas modificar algún campo.")
            nueva_cantidad = input("Introduce la nueva cantidad (deja en blanco para no modificar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = input("Introduce el nuevo precio (deja en blanco para no modificar): ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
