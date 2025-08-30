import producto
import empleados
import producto
import ventas


print("Menu principal")

seleccion =""
while seleccion != "0":
    print("1.Productos")
    print("2.Empleados")
    print("3.proveedores")
    print("4 ventas")
    print("0. salir")

    print("0. salir")
    seleccion =input("Selecciona una opcion: ")


    match seleccion:
        case"1":
            producto.menu_productos()

        case"2":
            empleados.menuEmpleados()

        case"3":
            pass

        case"4":
            menuVenas()

        case "0":
            print("saliendo del sistema")
















