import clientes
import empleados

def cargar_productos():
    productos = {}
    try:

        with open("productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    (id_producto, nombre, precio, id_categoria,total_compras, total_ventas, stock) = linea.split(":")
                    productos[id_producto] = {
                        "Nombre": nombre,
                        "Precio": float(precio),
                        "Categoria": id_categoria,
                        "TotalCompras": int(total_compras),
                        "TotalVentas": int(total_ventas),
                        "Stock": int(stock)
                    }
    except FileNotFoundError:
        pass

    return productos


def guardar_productos(producto):
    with open("ventas.txt","w", encoding="utf-8") as archivo:
        for ipd, datos in producto.items():
            archivo.write(
                f"{ipd}:{datos['Nombre']}:{datos['Precio']}:{datos['Categoria']}:"
                f"{datos['TotalCompras']}:{datos['TotalVentas']}:{datos['Stock']}\n"
            )


def cargar_cliente():
    cliente={}
    try:
        with open("ventas.txt","r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    nit,nombre,direccion,telefono,correo =linea.strip(":")
                    clientes[int(nit)]={
                        "Nombre": nombre,
                        "Direccion": direccion,
                        "Telefono": telefono,
                        "Correo": correo
                    }
    except FileNotFoundError:
        pass
    return cliente




class ventas:
    def __init__(self):
        self.empleados={}
        self.clientes=cargar_cliente()
        self.productos=cargar_productos()
        self.ventasRealizadas=[]

    def RealizarVentas(self):

        idEmpleado=input("Ingrese el ID del empelado: ")
        if idEmpleado in self.empleados:
            print("El empelado no existe")
            return


        nit=input("NIT: ")
        if nit =="":
            nit ="CF"
            if nit not in self.clientes:
                self.clientes[nit]= {"nombre": "consumidr final"}
        elif nit not in self.clientes:
            opcion=input("no registrado, desea registar s/n").lower()
            if opcion == "s":
                nuevo_cliente = clientes.registroClientes()
                self.clientes[nit] = nuevo_cliente
            else:
                nit="CF"
                if nit not in self.clientes:
                    self.clientes[nit]={"nombre": "consumidr final"}

        cliente =self.clientes[nit]
        print(f"cliente: {cliente['Nombre']}")


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
        guardar_productos(self.productos)

        venta = {
            "Empleado": idEmpleado,
            "cliente": cliente,
            "producto": producto,
            "cantidad": cantidad,
            "subtotal": subtotal,

        }
        self.ventasRealizadas.append(venta)








def menuVentas():
    admintracion_ventas=ventas()

    seleccion=""
    while seleccion != "0":
        print("\n Menu ventas")
        print("1. realizar ventas")
        print("0. volver")
        seleccion=input()

        match seleccion:
            case"1":
                admintracion_ventas.RealizarVentas()
            case"0":
                print("Volver")









