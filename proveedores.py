class Proveedor:
    def __init__(self, id_proveedor,nombreProveedores,direccionP,telefonoP,correoP):
        self.id_proveedor = id_proveedor
        self.nombreProveedores = nombreProveedores
        self.direccionP = direccionP
        self.telefonoP = telefonoP
        self.correoP = correoP

    def mostrarProveedor(self):
        print(self.id_proveedor,self.nombreProveedores,self.direccionP,self.telefonoP,self.correoP)
