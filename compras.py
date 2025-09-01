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
    except Exception:
        print(f"poductos vacios")
    return productos

def guardar_productos(productos):
    try:
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for id_producto, datos in productos.items():
                archivo.write(
                    f"{id_producto}:{datos['Nombre']}:{datos['Precio']}:{datos['Categoria']}:"
                    f"{datos['TotalCompras']}:{datos['TotalVentas']}:{datos['Stock']}\n"
                )
    except Exception:
        print(f" no encontrado" )
