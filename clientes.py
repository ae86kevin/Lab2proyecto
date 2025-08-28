class Clientes:
    def __init__(self,nit,nombre, direccion, telefono,correo):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo






class registroClientes:
    def __int__(self):
        self.DiccClientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(",")
                        self.DiccClientes[nit]={
                            "Nombre":nombre,
                            "Direccion":direccion,
                            "Telefono":telefono,
                            "Correo":correo
                        }
            print("Clientes impotodos dedsde.txt")
        except FileNotFoundError:
            print("no existe el clientes en la base de datos")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit,datos in self.DiccClientes.items():
                archivo.write(f"{nit}:{datos['Nombre']}:{datos['direccion']}:{datos['Telefono']}:{datos['Correo']}\n")



    def registroClientes(self):
        while True:
            try:
                nit = int(input("NIT: "))
                if nit == "":
                    print("NIT no puede estar vacio")
                    continue
                if nit in self.DiccClientes:
                    print("El cliente ya existe")
                    continue
            except ValueError:
                print("NIT unicamente son numers")

        nombre = input("Nombre: ")
        if nombre == "":
            print("Nombre no puede estar vacio")

        direccion = input("Direccion: ")
        if direccion == "":
            print("Direccion no puede estar vacio")

        telefono = input("Telefono: ")
        if telefono == "":
            print("Telefono no puede estar vacio")

        correo = input("Correo: ")
        if correo == "":
            print("Correo no puede estar vacio")

        nuevoClientes=Clientes(nit,nombre,direccion,telefono,correo)
        self.DiccClientes[nit] = nuevoClientes
        print("cliente registrado")










