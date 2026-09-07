from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n===== RESTAURANTE APP =====")
    print("1. Mostrar productos")
    print("2. Buscar producto por código")
    print("3. Registrar producto")
    print("4. Mostrar usuarios")
    print("5. Buscar usuario por identificación")
    print("6. Registrar usuario")
    print("7. Realizar venta")
    print("8. Consultar ventas de un usuario")
    print("0. Salir")


def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            restaurante.mostrar_productos()

        elif opcion == "2":
            codigo = input("Ingrese el código del producto: ")
            producto = restaurante.buscar_producto(codigo)

            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))

            restaurante.registrar_producto(
                codigo, nombre, precio, stock
            )

        elif opcion == "4":
            restaurante.mostrar_usuarios()

        elif opcion == "5":
            identificacion = input("Ingrese la identificación: ")
            usuario = restaurante.buscar_usuario(identificacion)

            if usuario:
                print(usuario)
            else:
                print("Usuario no encontrado.")

        elif opcion == "6":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")

            restaurante.registrar_usuario(
                identificacion, nombre
            )

        elif opcion == "7":
            identificacion = input("Identificación del usuario: ")
            codigo = input("Código del producto: ")
            cantidad = int(input("Cantidad: "))

            restaurante.realizar_venta(
                identificacion, codigo, cantidad
            )

        elif opcion == "8":
            identificacion = input("Identificación del usuario: ")

            ventas = restaurante.consultar_ventas_usuario(
                identificacion
            )

            if ventas:
                print("\nVentas del usuario:")
                for venta in ventas:
                    print(venta)
            else:
                print("No existen ventas para este usuario.")

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()