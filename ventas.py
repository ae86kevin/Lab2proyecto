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
        print(f"empleado: {empleado.nombreEmpleado}")

        nit =int(input("Ingrese el nit: "))
        if nit not in self.clientes:
            print("Clinte no registraod")
            opcion =input("Quire registar al clietne S/N: ").lower()
            if opcion == "s":
                nuevoCliente=clientes.registroClientes()
                self.clientes[nit]=nuevoCliente
            else:
                nit ="CF"
                if "CF" not in self.clientes:
                    self.clientes[nit]={"nombre": "consumidor final"}
        cliente=self.clientes[nit]
        print(f"cliente: {cliente['nombre']}")

        id_producto=int(input("Ingrese el ID del producto: "))
        if id_producto not in self.productos:
            print("Producto no existe")
            return

        producto=self.productos[id_producto]
        print(f"producto: {producto['nombre']}")


        try:
            cantidad=int(input("cantidad vendida: "))
            if cantidad > producto["stock"]:
                print("no hay suficiente en stock")
                return
        except ValueError:
            print("cantidad invalido")
            return

        subtotal =cantidad*producto["Precio"]

        producto["Stock"]-=cantidad
        producto["TotalVentas"]+= cantidad

        venta = {
            "Empleado": empleado.nombreEmpleado,
            "Cliente": cliente["Nombre"],
            "Producto": producto["Nombre"],
            "Cantidad": cantidad,
            "Subtotal": subtotal
        }
        self.ventasRealizadas.append(venta)

        print(" Venta registrada ")
        print(f"Total a pagar: Q.{subtotal:.2f}")










