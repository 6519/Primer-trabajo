class Emp:
    def Pedir_datos(self):
        self.clav=raw_input("Introduce la clave:")
        self.nom=raw_input("Nombre de usuario:")
        self.dir=raw_input("Introduce tu direccion:")
        self.edad=int(input("Introduce tu edad:"))
        self.tel=int(input("Agrega tu numero telefonico:"))
        self.horas=int(input("Introduce las horas trbajadas:"))
        self.pre=float(input("Ingresa el precio de una hora de trabajo:"))
        self.sueldo= self.horas*self.pre
    def Mostrar_datos(self):
        print "Tu nombre es =", self.nom
        print "Tu clave es =", self.clav
        print "Tu edad es =", self.edad
        print "Tu direccion es =", self.dir
        print "Tu numero telefonico es =", self.tel
        print "Tu sueldo es de =", self.sueldo,"pesos"
        print "El numero de horas que trabajaste son =", self.horas





