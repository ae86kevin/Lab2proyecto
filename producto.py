class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras=0, total_ventas=0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock


class Registros:
    def __init__(self):
        self.categorias={}
        self.productos={}



class ModificacionesProductos:
    def __init__(self,registrosAjustes):
        self.registrosAjustes = registrosAjustes

    def registrarProducto(self):


        while True:
            id_producto=input("Ingrese el id_producto: ")
            if id_producto == "":
                print("El id no puedes estar vacio")
            if id_producto in self.registros.productos:
                print("El producto ya existe")
                continue

            nombre = input("Ingrese el nombre: ")
            if nombre =="":
                print("El nombre no puedes estar vacio")

            while True:
                try:
                    precio = float(input("Ingrese el precio Q.: "))
                    if precio < 0:
                        print("El precio no puede ser menor a 0: intente de nuevo")
                    else:
                        break
                except ValueError:
                    print("Solo se permite numeros")


            while True:
                try:
                    stock = int(input("Ingrese el stock inicial: "))
                    if stock == "":
                        print("El stock no puedes estar vacio")
                    else:
                        break
                except ValueError:
                    print("Solo se permite numeros")


            id_categoria = input("Ingrese el id_categoria: ")
            if id_categoria == "":
                print("El id no puedes estar vacio")
                continue

            nuevoProducto=Producto(id_producto,nombre,precio,id_categoria,stock=stock)
            self.registros.agregarProducto(nuevoProducto)
            print("Producto registrado correctamente")


    def eliminarProducto(self):
        id_producto=input("Ingrese el id_producto: ")
        if id_producto in self.registros.productos:
            del(self.registros.productos[id_producto])
            print("Producto eliminado correctamente")
        else:
            print("El producto no existe")

    def ModificarProducto(self):
        id_producto=input("Ingrese el id_producto: ")
        if id_producto in self.registros.productos:
            print("producto no encontrado")
            return

        producto = self.registrosAjustes[id_producto]

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










