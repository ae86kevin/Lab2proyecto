class Proveedor:
    def __init__(self, id_proveedor,nombreProveedores,direccionP,telefonoP,correoP):
        self.id_proveedor = id_proveedor
        self.nombreProveedores = nombreProveedores
        self.direccionP = direccionP
        self.telefonoP = telefonoP
        self.correoP = correoP



class RegistroProveedores:
    def __init__(self):
        self.proveedores = {}
        self.cargarProveedores()

    def cargarProveedores(self):
        try:
            with open("prveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if linea.strip():
                        proveedor = proveedor.from_string(linea)
                        self.proveedores[proveedor.id_proveedor] = proveedor
            print("proveedores cargados")
        except FileNotFoundError:
            print("No existe el archivo prveedores.txt")

    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for id_proveedor, datos in self.proveedores.items():
                archivo.write(
                    f"{id_proveedor}:{datos['Nombre']}:{datos['Direccion']}:{datos['Telefono']}:{datos['Correo']}\n")



    def agregarProveedor(self):
        while True:
            id_proveedor = input("Ingresa el ID del proveedor: ").strip()
            if id_proveedor == "":
                print("El ID no puede estar vacío")
            if id_proveedor in self.proveedores:
                print("El ID ya existe, intenta con otro")
                continue
            break

        while True:
            nombre=input("Ingresa el nombre del proveedor: ")
            if nombre == "":
                print("El nombre no puede estar vacio ")
                continue
            break

        while True:
            direccion =input("Ingrese la direccion: ")
            if direccion== "":
                print("la direcion no puede estar vacio ")
                continue
            break

        while True:
            telefono=input("Ingresa el telefono: ")
            if telefono == "":
                print("el telefono no puede estar vacio")
                continue
            break

        while True:
            correo=input("Ingresa la correo: ")
            if correo == "":
                print("correo no puede estar vacion ")
                continue

            break

        self.proveedores[id_proveedor]={
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
            "correo": correo

        }

        self.guardar_proveedores()
        print("proveedores guardados")




    def mostrarProveedores(self):
        if self.proveedores:
            print("proveedores registrados")
            for id_proveedores,datos in self.proveedores.items():
                print(f"\n ID :{ id_proveedores }")
                for clave,valor in datos.items():
                    print(f"Clave : {clave}")


    def eliminarProveedor(self, id_proveedor):
        if id_proveedor in self.proveedores:
            del self.proveedores[id_proveedor]
            self.guardar_proveedores()
            print(f"proveedor eliminardo")
        else:
            print("no hay proveedores registrados")

def menuProveedores(adminProveedores):

    seleccion =""
    while seleccion != "0":
        print("\nMenu Proveedores")
        print("1.Agregar proveedores")
        print("2.Eliminar proveedores")
        print("3.Mostrar proveedores")
        print("0.Salir")
        seleccion=input()

        match seleccion:
            case "1":
                adminProveedores.agregarProveedor()
            case "2":
                id_proveedor = input("Ingresa el ID del proveedor: ")
                adminProveedores.eliminarProveedor(id_proveedor)
            case "3":
                adminProveedores.mostrarProveedor()
            case "0":
                print("Saliendo")
                break


