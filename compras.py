import os

def cargar_productos():
    productos = {}
    if not os.path.exists("productos.txt"):
        return productos
    try:
        with open("productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock = linea.split(":")
                    productos[id_producto] = {
                        "Nombre": nombre,
                        "Precio": float(precio),
                        "Categoria": id_categoria,
                        "TotalCompras": int(total_compras),
                        "TotalVentas": int(total_ventas),
                        "Stock": int(stock)
                    }
    except Exception as e:
        print(f"Error al cargar productos: {e}")
    return productos

def guardar_productos(productos):
    try:
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for id_producto, datos in productos.items():
                archivo.write(
                    f"{id_producto}:{datos['Nombre']}:{datos['Precio']}:{datos['Categoria']} :{datos['TotalCompras']}:{datos['TotalVentas']}:{datos['Stock']}\n"
                )
    except Exception:
        print(" no hay productos")




class Compras:
    def __init__(self):
        self.productos = cargar_productos()

    def realizar_compra(self):
        if not self.productos:
            print("No hay productos registrados.")
            return

        print(" Productos disponibles:")
        for id_producto, datos in self.productos.items():
            print(f"ID: {id_producto}  Nombre: {datos['Nombre']}  Precio: Q{datos['Precio']}  Stock: {datos['Stock']}")

        id_producto = input("Ingrese el ID del producto a comprar: ").strip()
        if id_producto not in self.productos:
            print("Producto no existe.")
            return

        producto = self.productos[id_producto]

        try:
            cantidad = int(input(f"Ingrese la cantidad a comprar de {producto['Nombre']}: "))
            if cantidad <= 0:
                print("Cantidad inválida.")
                return
        except ValueError:
            print("Cantidad inválida.")
            return


        producto["Stock"] += cantidad
        producto["TotalCompras"] += cantidad
        guardar_productos(self.productos)

        print(f"Compra registrada: {cantidad} unidades de {producto['Nombre']}")
        print(f"Nuevo stock: {producto['Stock']}")

