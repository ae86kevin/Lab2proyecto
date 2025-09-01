import os

class Empleados:
    def __init__(self, idEmpleado, nombreEmpleado, direccion, telefono, correo, puesto):
        self.idEmpleado = idEmpleado
        self.nombreEmpleado = nombreEmpleado
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto




class AdministracionEmpleados:
    def __init__(self):
        self.diccEmpleados = {}
        self.cargarEmpleados()






    def cargarEmpleados(self):
        if not os.path.exists("empleados.txt"):
            return
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        idEmpleado, nombre, direccion, telefono, correo, puesto = linea.split(":")
                        self.diccEmpleados[int(idEmpleado)] = Empleados(
                            int(idEmpleado), nombre, direccion, telefono, correo, puesto
                        )
        except Exception :
            print(f"no se encuentra registro ")







    def guardarEmpleados(self):
        try:
            with open("empleados.txt", "w", encoding="utf-8") as archivo:
                for idEmpleado, emp in self.diccEmpleados.items():
                    archivo.write(f"{idEmpleado}:{emp.nombreEmpleado}:{emp.direccion}:"
                                  f"{emp.telefono}:{emp.correo}:{emp.puesto}\n")
        except Exception:
            print(f"no se encuentra registro ")





    def registroEmpleados(self):
        while True:
            try:
                idEmpleado = int(input("\nIngrese el ID de Empleado: "))
                if idEmpleado in self.diccEmpleados:
                    print("El ID de Empleado ya existe ")
                    continue
            except ValueError:
                print("ID invalido")
                continue

            nombreEmpleado = input("ingrese el nombre del Empleado: ")
            if nombreEmpleado == "":
                print("El nombre del Empleado esta vacio")
                continue

            direccion = input("ingrese direccion del Empleado: ")
            if direccion == "":
                print("El direccion del Empleado esta vacio")
                continue

            telefono = input("ingrese el telefono del Empleado: ")
            if telefono == "":
                print("El telefono del Empleado esta vacio")
                continue

            correo = input("Ingrese el correo del Empleado: ")
            if correo == "":
                print("El correo del Empleado esta vacio")
                continue

            puesto = input("Ingrese el puesto del Empleado: ")
            if puesto == "":
                print("El puesto del Empleado esta vacio")
                continue




            nuevoEmpleado = Empleados(idEmpleado, nombreEmpleado, direccion, telefono, correo, puesto)
            self.diccEmpleados[idEmpleado] = nuevoEmpleado
            self.guardarEmpleados()
            print("El Empleado Registrado exitosamente")
            break




    def modificarEmpleado(self):
        try:
            idEmpleado = int(input("Ingrese el ID de Empleado: "))
        except ValueError:
            print("ID invalido")
            return

        if idEmpleado not in self.diccEmpleados:
            print("Empleado no encontrado")
            return





        empleado = self.diccEmpleados[idEmpleado]

        nuevoNombre = input("Nombre: ")
        if nuevoNombre == "":
            nuevoNombre = empleado.nombreEmpleado

        nuevaDireccion = input("Direccion del Empleado: ")
        if nuevaDireccion == "":
            nuevaDireccion = empleado.direccion

        nuevoTelefono = input("Ingrese el telefono del Empleado: ")
        if nuevoTelefono == "":
            nuevoTelefono = empleado.telefono

        nuevoCorreo = input("Ingrese el correo del Empleado: ")
        if nuevoCorreo == "":
            nuevoCorreo = empleado.correo

        nuevoPuesto = input("Ingrese el puesto del Empleado: ")
        if nuevoPuesto == "":
            nuevoPuesto = empleado.puesto



        empleado.nombreEmpleado = nuevoNombre
        empleado.direccion = nuevaDireccion
        empleado.telefono = nuevoTelefono
        empleado.correo = nuevoCorreo
        empleado.puesto = nuevoPuesto
        self.guardarEmpleados()
        print("Empleado modificado correctamente")






    def darDebaja(self):
        try:
            idEmpleado = int(input("Ingrese el ID de Empleado: "))
        except ValueError:
            print("ID invalido")
            return

        if idEmpleado in self.diccEmpleados:
            del self.diccEmpleados[idEmpleado]
            self.guardarEmpleados()
            print("Empleado dado de baja")
        else:
            print("Empleado no encontrado")

    def verEmpleados(self):
        if not self.diccEmpleados:
            print("No hay empleados registrados.")
            return

        print("\nListado de Empleados:")
        for idEmpleado, empleado in self.diccEmpleados.items():
            print(f"ID: {idEmpleado}  Nombre: {empleado.nombreEmpleado}  "
                  f"Dirección: {empleado.direccion}  Teléfono: {empleado.telefono}  "
                  f"Correo: {empleado.correo}  Puesto: {empleado.puesto}")





def menuEmpleados(adminEmpleados):
    seleccion = ""
    while seleccion != "0":
        print("\nMenu Empleados")
        print("1. Registrar empleado")
        print("2. Modificar información")
        print("3. Dar de baja")
        print("4. Ver empleados")
        print("0. Volver al menu")

        seleccion = input("Seleccione una opción: ")

        match seleccion:
            case "1":
                adminEmpleados.registroEmpleados()
            case "2":
                adminEmpleados.modificarEmpleado()
            case "3":
                adminEmpleados.darDebaja()
            case "4":
                adminEmpleados.verEmpleados()
            case "0":
                print("Volver al menu")
