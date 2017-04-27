class Al:

    def Pedir_datos(self):
        self.numc=raw_input("Introduce tu numero de control:")
        self.nom=raw_input("Nombre de usuario:")
        self.edad=int(input("Ingresa tu edad:"))
        self.dir=raw_input("Ingresa tu direccion:")
        self.tel=int(input("Agrega tu numero de telefono:"))
    def Mostrar_datos(self):
        print "Tu nombre de usuario es =",self.nom
        print "El numero de control es =",self.numc
        print "Tu edad es =", self.edad
        print "Tu direccion es =", self.dir
        print "Tu numero telefonico es =", self.tel
    def Pedir_calif(self):
        self.cal1=float(input("Dame la primera calificacion:"))
        self.cal2=float(input("Dame la segunda calificacion:"))
        self.cal3=float(input("Dame la tercera calificacion:"))
        self.promedio= (self.cal1 + self.cal2 + self.cal3) / 3
    def Mostrar_promedio(self):
        print "Tu promedio es =", self.promedio

