import compras
import producto
import empleados
import producto
import proveedores
import ventas

adminEmpleados = empleados.AdministracionEmpleados()

print("\nMenu principal")

seleccion =""
while seleccion != "0":
    print("1. Productos")
    print("2. Empleados")
    print("3. proveedores")
    print("4  ventas")
    print("5. Compas")

    print("0. salir")


    seleccion =input("Selecciona una opcion: ")


    match seleccion:
        case"1":
            producto.menu_productos()

        case"2":
            empleados.menuEmpleados(adminEmpleados)

        case"3":

            proveedores.menuProveedores()

        case"4":
            ventas.menuVentas(adminEmpleados)
        case"5":
            compras.menuCompras()

        case "0":
            print("saliendo del sistema")


















