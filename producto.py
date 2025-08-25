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

    def agregarProducto(self,producto):
        self.productos[producto.id_producto] = producto

    def elimarProducto(self,id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]

    def obtenerProductos(self, id_producto):
        if id_producto in self.productos:
            return self.productos[id_producto]
        else:
            return None


