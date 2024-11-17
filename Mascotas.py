class Mascota:
    def __init__(self, raza, edad):
        self.raza = raza
        self.edad = edad 
        print ("DATOS DE MASCOTA")

    def info (self):
        presentacion = ("La raza del perro es un {} y tiene {}".format(self.raza, self.edad))
        

    def eat (self, tiempo, comida ):
        self. tiempo = tiempo
        self.comida = comida
        

    def sleep (self, dormir):
        self.dormir = dormir 
        print ("La raza del perro es {} y tiene {} años, come {} a las {}pm y su horario de descanso es a las {} pm. ".format(self.raza, self.edad, self.comida, self.tiempo, self.dormir))

perro1 = Mascota ("bulldog", 4)
perro1.info()
perro1.eat(7, "pollo")
perro1.sleep(9)
perro2 = Mascota ("chihuahua", 6)
perro2.info()
perro2.eat(6, "croquetas")
perro2.sleep(8)
perro3 = Mascota ("husky", 2)
perro3.info()
perro3.eat(8, "pollo")
perro3.sleep(10)
