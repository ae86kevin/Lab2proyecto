import producto

print("Menu principal")

seleccion =""
while seleccion != "0":
    print("1.Productos")
    print("0. salir")
    seleccion =input("Selecciona una opcion: ")


    match seleccion:
        case "1":
            producto.menu_productos()



