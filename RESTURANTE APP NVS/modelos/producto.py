class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )