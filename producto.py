class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Producto:
    def __init__(self):
        self.productos={}
        self.cargarProductos()

    def cargarProductos(self):
        try:
            with open ('productos.txt', 'r',encoding='utf-8') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        (id_producto, nombre, precio, id_categoria,total_compras, total_ventas, stock) = linea.split(":")
                        self.productos[id_producto] = {
                            "Nombre":nombre,
                            "precio":float(precio),
                            "categoria":id_categoria,
                            "total_compras": int(total_compras),
                            "total_ventas":int(total_ventas),
                            "stock":int(stock)
                        }
            print("Productos importados desde productos.txt")
        except FileNotFoundError:
            print("No existe el archivo productos.txt")

    def guardarProductos(self):
        with open("productos.txt","w",encoding="utf-8") as archivo:
            for id_producto, datos in self.productos.items():
                archivo.write(
                    f"{id_producto}:{datos['Nombre']}:{datos['Precio']}:{datos['Categoria']}:{datos['TotalCompras']}:{datos['TotalVentas']}:{datos['Stock']}\n"
                )

class  AdministracionProductos:
    def __init__(self,registos:Producto):
        self.registos=registos

    def agregarProducto(self ):
        while True:
            id_produto=input("Ingresa el id_producto: ")
            if id_produto=="":
                print("el Id no puede estasr vacio")
                continue
            if id_produto in self.registos.produtos:
                print("El id_producto ya existe")
                continue
            break


        while True:
            nombre=input("Ingresa el nombre: ")
            if nombre =="":
                print("El nombre no puede estasr vacio")
                continue
            break

        while True:
            try:
                precio=float(input("Ingresa el precio: "))
                if precio < 0:
                    print("El precio no puede ser mayor que 0")
                    continue
                break
            except ValueError:
                print("precio invaalido")


        while True:
            try:
                stock=int(input("Ingresa el stock: "))
                if stock < 0:
                    print("El stock no puede ser mayor que 0")
                    continue
                break
            except ValueError:
                print("stock invalido")



        while True:
            id_categoria = input("Ingresa el id_categoria: ")
            if id_categoria == "":
                print("El id_categoria no puede estasr vacio")
                continue
            break

        self.registros.productos[id_producto] = {
            "Nombre": nombre,
            "Precio": precio,
            "Categoria": id_categoria,
            "TotalCompras": 0,
            "TotalVentas": 0,
            "Stock": stock
        }
        self.registros.guardarProductos()
        print(" Producto agregado correctamente")








    def eliminarProducto(self):
        id_producto=input("Ingrese el id_producto: ")
        if id_producto in self.registros.productos:
            del(self.registros.productos[id_producto])
            print("Producto eliminado correctamente")
        else:
            print("El producto no existe")

    def ModificarProducto(self):
        id_producto=input("Ingrese el id_producto: ")
        if id_producto not in self.registros.productos:
            print("El producto no existe")
            return

        producto = self.registros.productos[id_producto]

        nuevoNombre = input("Ingrese el nombre: ")
        if nuevoNombre == "":
            print("El nombre no puedes estar vacio")
            nuevoNombre = producto.nombre


        while True:
            try:
                nuevoPrecio = float(input("Ingrese el precio Q.: "))
                if nuevoPrecio=="":
                    print("El precio no puedes estar vacio")
                else:
                    nuevoPrecio=producto.precio
                    break
            except ValueError:
                print("Solo se permite numeros")


        while True:
            try:
                stockActulizado = int(input("Ingrese el stock actulizado: "))
                if stockActulizado == "":
                    print("El stock no puedes estar vacio")
                else:
                    stockActulizado=producto.stock
                    break
            except ValueError:
                print("Solo se permite numeros")

        producto.nombre = nuevoNombre
        producto.precio = nuevoPrecio
        producto.stock = stockActulizado
        print("Producto modificado correctamente")



def menu_productos():
    registros=Producto()
    modificaciones=AdministracionProductos(registros)

    selecion = ""
    while selecion != "0":
        print("\n Menu de Productos")
        print("1. Registrar Producto")
        print("2. Elimaar Producto")
        print("3. Modificar Producto")
        print("4. Volver al menu")
        selecion=input()

        match selecion:
            case "1":
                modificaciones.agregarProducto()
            case "2":
                modificaciones.eliminarProducto()
            case "3":
                modificaciones.ModificarProducto()
            case "0":
                print("volver al menu")







