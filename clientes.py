class Clientes:
    def __int__(self):
        self.clientes = {}
        self.cargarClientes()

    def cargarClientes(self):
        try:
            with open("clientes.txt", "r",encoding="utf-8") as archivo:
                for linea in archivo
                    linea = linea.strip()
                    if linea:
                        nit,nombre,direccion,tele



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


        self.clienes[nit]={
            "Nombre":nombre,
            "Direccion":direccion,
            "Telefono":telefono,
            "Correo":correo
        }

        self.guardar_clientes()
        print("cliente registrado")








