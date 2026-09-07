class Venta:
    def __init__(self, identificacion_usuario, codigo_producto, cantidad):
        self.identificacion_usuario = identificacion_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad

    def __str__(self):
        return (
            f"Usuario: {self.identificacion_usuario} | "
            f"Producto: {self.codigo_producto} | "
            f"Cantidad: {self.cantidad}"
        )