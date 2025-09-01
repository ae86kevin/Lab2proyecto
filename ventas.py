import clientes
import empleados

def cargar_productos():
    productos = {}
    try:
        with open("productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    (id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock) = linea.split(":")
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

def guardar_productos(productos):
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for ipd, datos in productos.items():
            archivo.write(
                f"{ipd}:{datos['Nombre']}:{datos['Precio']}:{datos['Categoria']}:"
                f"{datos['TotalCompras']}:{datos['TotalVentas']}:{datos['Stock']}\n"
            )

def cargar_clientes():
    clientes_dict = {}
    try:
        with open("clientes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    nit, nombre, direccion, telefono, correo = linea.split(":")
                    clientes_dict[nit] = {
                        "Nombre": nombre,
                        "Direccion": direccion,
                        "Telefono": telefono,
                        "Correo": correo
                    }
    except FileNotFoundError:
        pass
    return clientes_dict


class Ventas:
    def __init__(self, adminEmpleados: empleados.AdministracionEmpleados):
        self.empleados = adminEmpleados.diccEmpleados
        self.clientes = cargar_clientes()
        self.productos = cargar_productos()
        self.ventasRealizadas = []

    def realizar_venta(self):
        while True:
            try:
                idEmpleado = int(input("Ingrese el ID del empleado: "))
                if idEmpleado in self.empleados:
                    empleado_actual = self.empleados[idEmpleado]
                    print(f"Empleado: {empleado_actual.nombreEmpleado} | Puesto: {empleado_actual.puesto}")
                    break
                print("Empleado no encontrado. Intenta nuevamente.")
            except ValueError:
                print("ID inválido. Intenta nuevamente.")

        nit = input("Ingrese el NIT del cliente: ").strip()
        if nit == "":
            nit = "CF"

        if nit not in self.clientes and nit != "CF":
            opcion = input("Cliente no registrado. Desea registrarlo? (s/n): ").lower()
            if opcion == "s":
                registro = clientes.registroClientes()
                nuevo_cliente = registro.registrarCliente()
                self.clientes[nit] = nuevo_cliente
            else:
                nit = "CF"

        cliente_actual = self.clientes.get(nit, {"Nombre": "Consumidor Final"})
        print(f"Cliente seleccionado: {cliente_actual['Nombre']}")


        id_producto = input("Ingrese el ID del producto: ")
        if id_producto not in self.productos:
            print("Producto no existe.")
            return
        producto_actual = self.productos[id_producto]
        print(f"Producto: {producto_actual['Nombre']} | Stock disponible: {producto_actual['Stock']}")


        try:
            cantidad = int(input("Cantidad a vender: "))
            if cantidad > producto_actual["Stock"]:
                print("No hay suficiente stock.")
                return
        except ValueError:
            print("Cantidad inválida.")
            return

        subtotal = cantidad * producto_actual["Precio"]
        producto_actual["Stock"] -= cantidad
        producto_actual["TotalVentas"] += cantidad
        guardar_productos(self.productos)

        venta = {
            "Empleado": empleado_actual,
            "Cliente": cliente_actual,
            "Producto": producto_actual,
            "Cantidad": cantidad,
            "Subtotal": subtotal
        }
        self.ventasRealizadas.append(venta)
        print(f"Venta registrada. Subtotal: Q{subtotal}")


def menuVentas(adminEmpleados):
    admin_ventas = Ventas(adminEmpleados)
    seleccion = ""
    while seleccion != "0":
        print("\nMenu Ventas")
        print("1. Realizar venta")
        print("0. Volver")
        seleccion = input("Seleccione opción: ")

        match seleccion:
            case "1":
                admin_ventas.realizar_venta()
            case "0":
                print("Volviendo al menú principal")
