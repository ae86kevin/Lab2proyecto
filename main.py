import producto

print("Menu principal")

seleccion =""
while seleccion != "0":
    print("1.Proveedores")
    print("0. salir")
    seleccion =input("Selecciona una opcion: ")


    match seleccion:
        case "1":
