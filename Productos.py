class Product:
    def Datos(self):
        self.clave = int(input("Introduce la clave del producto:"))
        self.nombre = raw_input("Introduce el nombre del producto:")
        self.desc = raw_input("Describe las caracteristicas del producto:")
        self.costo = float(input("Introduce el valor del producto:"))
        self.cantidad = int(input("Cuantas unidades son?:"))

    def Mostrar(self):
        print "El nombre del producto es =", self.nombre
        print "La clave del producto es =", self.clave
        print "Las caracteristicas son =", self.desc
        print "La cantidad de productos es =", self.cantidad
        print "El valor por unidad es =", self.costo

    def Calcular(self):
        self.venta = self.cantidad * self.costo
        print "El total por la venta es de =", self.venta
