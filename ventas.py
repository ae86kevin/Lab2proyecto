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




class Ventas:
    def __init__(self, adminEmpleados: empleados.AdministracionEmpleados):
        self.empleados = adminEmpleados.diccEmpleados
        self.clientes = cargar_cliente()
        self.productos = cargar_productos()
        self.ventasRealizadas = []

        while True:
            try:
                idEmpleado_input = input("Ingrese el ID del empleado: ")
                idEmpleado = int(idEmpleado_input)
                if idEmpleado in self.empleados:
                    print(f"Empleado: {self.empleados[idEmpleado].nombreEmpleado}")
                    break
                print("Empleado no encontrado. Intenta nuevamente.")
            except ValueError:
                print("ID inválido. Intenta nuevamente.")

        nit = input("NIT del cliente: ").strip()
        if nit == "":
            nit = "CF"
        if nit not in self.clientes and nit != "CF":
            opcion = input("Cliente no registrado. Desea registrarlo? (s/n): ").lower()
            if opcion == "s":
                nuevo_cliente = clientes.registroClientes()
                self.clientes[nit] = nuevo_cliente
            else:
                nit = "CF"

        cliente = self.clientes.get(nit, {"Nombre": "Consumidor Final"})
        print(f"Cliente seleccionado: {cliente['Nombre']}")

        id_producto = input("ID del producto: ")
        if id_producto not in self.productos:
            print("Producto no existe.")
            return
        producto = self.productos[id_producto]
        print(f"Producto: {producto['Nombre']} | Stock disponible: {producto['Stock']}")

        try:
            cantidad = int(input("Cantidad a vender: "))
            if cantidad > producto["Stock"]:
                print("No hay suficiente stock.")
                return
        except ValueError:
            print("Cantidad inválida.")
            return


        subtotal = cantidad * producto["Precio"]
        producto["Stock"] -= cantidad
        producto["TotalVentas"] += cantidad
        guardar_productos(self.productos)

        venta = {
            "Empleado": idEmpleado,
            "Cliente": cliente,
            "Producto": producto,
            "Cantidad": cantidad,
            "Subtotal": subtotal
        }
        self.ventasRealizadas.append(venta)
        print(f"Venta registrada. Subtotal: Q{subtotal}")


        print(f"producto: {producto['nombre']}")







def menuVentas(adminEmpleados):
    admin_ventas = Ventas(adminEmpleados)
    seleccion = ""
    while seleccion != "0":
        print("\n--- Menu Ventas ---")
        print("1. Realizar venta")
        print("0. Volver")
        seleccion = input("Seleccione opción: ")

        match seleccion:
            case "1":
                admin_ventas.realizar_venta()
            case "0":
                print("Volviendo al menú principal")






