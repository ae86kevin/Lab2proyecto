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
                idEmpleado = int(input("Ingrese el ID de Empleado: "))
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








