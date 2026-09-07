from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self):
        self.archivo = ArchivoServicio()

        # Colecciones principales
        self.productos = []
        self.usuarios = []
        self.ventas = []

        # Índices auxiliares para búsquedas rápidas
        self.indice_productos = {}
        self.indice_usuarios = {}
        self.ventas_por_usuario = {}

        self.cargar_datos()

    # =========================
    # CARGAR DATOS
    # =========================

    def cargar_datos(self):
        datos_productos = self.archivo.cargar("productos.json")
        datos_usuarios = self.archivo.cargar("usuarios.json")
        datos_ventas = self.archivo.cargar("ventas.json")

        self.productos = [
            Producto(
                producto["codigo"],
                producto["nombre"],
                producto["precio"],
                producto["stock"]
            )
            for producto in datos_productos
        ]

        self.usuarios = [
            Usuario(
                usuario["identificacion"],
                usuario["nombre"]
            )
            for usuario in datos_usuarios
        ]

        self.ventas = [
            Venta(
                venta["identificacion_usuario"],
                venta["codigo_producto"],
                venta["cantidad"]
            )
            for venta in datos_ventas
        ]

        self.reconstruir_indices()

    # =========================
    # RECONSTRUIR ÍNDICES
    # =========================

    def reconstruir_indices(self):
        self.indice_productos = {
            producto.codigo: producto
            for producto in self.productos
        }

        self.indice_usuarios = {
            usuario.identificacion: usuario
            for usuario in self.usuarios
        }

        self.ventas_por_usuario = {}

        for venta in self.ventas:
            if venta.identificacion_usuario not in self.ventas_por_usuario:
                self.ventas_por_usuario[venta.identificacion_usuario] = []

            self.ventas_por_usuario[
                venta.identificacion_usuario
            ].append(venta)

    # =========================
    # PRODUCTOS
    # =========================

    def registrar_producto(self, codigo, nombre, precio, stock):
        if codigo in self.indice_productos:
            print("Ya existe un producto con ese código.")
            return False

        producto = Producto(codigo, nombre, precio, stock)

        self.productos.append(producto)
        self.indice_productos[codigo] = producto

        self.guardar_productos()

        print("Producto registrado correctamente.")
        return True

    def buscar_producto(self, codigo):
        return self.indice_productos.get(codigo)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            print(producto)

    # =========================
    # USUARIOS
    # =========================

    def registrar_usuario(self, identificacion, nombre):
        if identificacion in self.indice_usuarios:
            print("Ya existe un usuario con esa identificación.")
            return False

        usuario = Usuario(identificacion, nombre)

        self.usuarios.append(usuario)
        self.indice_usuarios[identificacion] = usuario

        self.guardar_usuarios()

        print("Usuario registrado correctamente.")
        return True

    def buscar_usuario(self, identificacion):
        return self.indice_usuarios.get(identificacion)

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        for usuario in self.usuarios:
            print(usuario)

    # =========================
    # VENTAS
    # =========================

    def realizar_venta(self, identificacion_usuario, codigo_producto, cantidad):
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None:
            print("Usuario no encontrado.")
            return False

        if producto is None:
            print("Producto no encontrado.")
            return False

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return False

        if producto.stock < cantidad:
            print("Stock insuficiente.")
            return False

        venta = Venta(
            identificacion_usuario,
            codigo_producto,
            cantidad
        )

        self.ventas.append(venta)

        # Actualizar stock
        producto.actualizar_stock(-cantidad)

        # Actualizar índice de ventas por usuario
        if identificacion_usuario not in self.ventas_por_usuario:
            self.ventas_por_usuario[identificacion_usuario] = []

        self.ventas_por_usuario[identificacion_usuario].append(venta)

        self.guardar_productos()
        self.guardar_ventas()

        print("Venta realizada correctamente.")
        return True

    def consultar_ventas_usuario(self, identificacion_usuario):
        return self.ventas_por_usuario.get(identificacion_usuario, [])

    # =========================
    # GUARDAR DATOS
    # =========================

    def guardar_productos(self):
        datos = [
            {
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            }
            for producto in self.productos
        ]

        self.archivo.guardar("productos.json", datos)

    def guardar_usuarios(self):
        datos = [
            {
                "identificacion": usuario.identificacion,
                "nombre": usuario.nombre
            }
            for usuario in self.usuarios
        ]

        self.archivo.guardar("usuarios.json", datos)

    def guardar_ventas(self):
        datos = [
            {
                "identificacion_usuario": venta.identificacion_usuario,
                "codigo_producto": venta.codigo_producto,
                "cantidad": venta.cantidad
            }
            for venta in self.ventas
        ]

        self.archivo.guardar("ventas.json", datos)