class Clientes:
    def __init_(self):
        self.clientes = {}
        self.cargarClientes()

    def cargarClientes(self):
        try:
            with open("clientes.txt", "r",encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit,nombre,direccion,telefono,correo= linea.split(",")
                        self.clientes[int(nit)] = {
                            "Nombre": nombre,
                            "Direccion": direccion,
                            "telefono": telefono,
                            "Correo": correo
                        }
        except FileNotFoundError:
            print("no existe el archivo")
            with open("clientes.txt", "w",encoding="utf-8"):
                pass

    def guardarClientes(self):
        with open("clientes.txt", "w",encoding="utf-8") as archivo:
            for nit,datos in self.clientes.items():
                linea = f"{nit},{datos['Nombre']},{datos['Direccion']},{datos['Telefono']},{datos['Correo']}\n"
                archivo.write(linea)


def registroClientes(self):
        while True:
            try:
                nit = int(input("NIT: "))
                if nit == "":
                    print("NIT no puede estar vacio")
                    continue
                if nit in self.clienes:
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


        self.clientes[nit]={
            "Nombre":nombre,
            "Direccion":direccion,
            "Telefono":telefono,
            "Correo":correo
        }

        self.guardarClienes()
        print("cliente registrado")








