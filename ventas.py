import clientes
class ventas:
    def __init__(self,empleados,clientes,productos):
        self.empleados = empleados
        self.clientes = clientes
        self.productos = productos
        self.ventasRealizadas =[]

    def RealizarVentas(self):

        idEmpleado=input("Ingrese el ID del empelado: ")
        if idEmpleado in self.empleados:
            print("El empelado no existe")
            return
        empleado=self.empleados[idEmpleado]
        print(f"empleado: {empleado.nombre}")

        nit=input("Ingrese el nit: ")
        if nit not in self.clientes:
            opcion = input("Cliente no registado")
            print("Desea Registar s/n")
            if opcion == "s":
                nuevoCliente =clientes.registroClientes()
                self.clientes[nit]=nuevoCliente
            else:
                nit = "CF"
                if "CF" not in self.clientes:
                    self.clientes[nit]=clientes.Cliente("consumidor final")
        cliente=self.clientes[nit]
        print(f"Cliete: {cliente.nombre}")






