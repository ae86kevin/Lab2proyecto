class Empleados:
    def __init__(self,idEmpleado,nombreEmpleado,direccion,telefono,correo,puesto):
        self.idEmpleado = idEmpleado
        self.nombreEmpleado = nombreEmpleado
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto

    def mostrarEmpleado(self):
        return self.IdEmpleado,self.NombreEmpleado,self.direccion,self.telefono,self.correo,self.puesto

class AdministracionEmpleados:
    def __int__(self):
        self.diccEmpleados = {}

    def registroEmpleados(self):
        while True:
            try:
                idEmpleado = int(input("\nIngrese el ID de Empleado: "))
                if idEmpleado == "":
                    print("El ID del empleado esta vacio ")
                    continue
                if idEmpleado in self.diccEmpleados:
                    print("El ID de Empleado ya existe ")
                    continue
            except ValueError:
                print("ID invalido")


            nombreEmpleado = input("Ingrese el nombre del Empleado: ")
            if nombreEmpleado == "":
                print("El nombre del Empleado esta vacio")
                continue


            direccion=input("Ingrese direccion del Empleado: ")
            if direccion == "":
                print("El direccion del Empleado esta vacio")
                continue

            telefono=input("Ingrese el telefono del Empleado: ")
            if telefono == "":
                print("El telefono del Empleado esta vacio")
                continue

            correo=input("Ingrese el correo del Empleado: ")
            if correo == "":
                print("El correo del Empleado esta vacio")
                continue


            puesto=input("Ingrese el puesto del Empleado: ")
            if puesto == "":
                print("El puesto del Empleado esta vacio")
                continue


            nuevoEmpleado =Empleados(idEmpleado,nombreEmpleado,direccion,telefono,correo,puesto)
            self.diccEmpleados[idEmpleado] = nuevoEmpleado
            print("El Empleado Registrado exitosamente")
            break

    def modificarEmpleado(self):
        idEmpleado = int(input("\nIngrese el ID de Empleado: "))
        if idEmpleado in self.diccEmpleados:
            print("Emplado no encotrado")
            return


        empleado=self.diccEmpleados[idEmpleado]

        nuevoNombre=input("Nombre: ")
        if nuevoNombre =="":
            print("El nombre no puedes estar vacio")
            nuevoNombre=empleado.nombreEmpleado

        nuevaDireccion=input("Direccion del Empleado: ")
        if nuevaDireccion == "":
            print("la direccion no puede estasr vacia")
            nuevaDireccion=empleado.direccionP

        nuevoTelefono=input("ingrese el telefono del Empleado: ")
        if nuevoTelefono == "":
            print("El telefono no puedes estar vacio")
            nuevoTelefono=empleado.telefonoP

        nuevoCorreo=input("ingrese el correo del Empleado: ")
        if nuevoCorreo == "":
            print("El correo no puedes estar vacio")
            nuevoCorreo=empleado.correoP

        nuevoPuesto=input("ingrese el puesto del Empleado: ")
        if nuevoPuesto =="":
            print(" no puedes vacio ")
            nuevoPuesto=empleado.puesto

        empleado.nombreEmpleado=nuevoNombre
        empleado.direccionP=nuevaDireccion
        empleado.telefonoP=nuevoTelefono
        empleado.correoP=nuevoCorreo
        empleado.puesto=nuevoPuesto

    def darDebaja(self):
        idEmpleado=int(input("Ingrese el ID de Empleado: "))
        if idEmpleado in self.diccEmpleados:
            del self.diccEmpleados[idEmpleado]
            print("El Empleado Registrado exitosamente")
        else:
            print("Emplado no encontraod")


def menuEmpleados():
    modificacionesEmpelados=AdministracionEmpleados()

    seleccion = ""
    while seleccion != "0":
        print("\nMenu Empleados")
        print("1. Registrar emeplado")
        print("2. Modificicar informacion")
        print("3. Dar debaja")
        print("0. Volver al menu")
        seleccion=input("seleccione una opcion: ")

        match seleccion:
            case "1":
                modificacionesEmpelados.registroEmpleados()
            case"2":
                modificacionesEmpelados.modificarEmpleado()
            case"3":
                modificacionesEmpelados.darDebaja()
            case"0":
                print("Volver al menu")













