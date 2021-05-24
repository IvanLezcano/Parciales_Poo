class Pajaro:
    def __init__(self,fuerza,ira):
        self.fuerza = fuerza
        self.ira= ira

    def enojarse(self):
        self.ira = self.ira*2
        return None


class PajaroComun(Pajaro):
    def __init__(self, fuerza, ira):
        super().__init__(fuerza, ira)
        self.fuerza= self.ira * 2
        


class Bomb(PajaroComun):
    def __init__(self, fuerza, ira):
        super().__init__(fuerza, ira)
        self.topeActual = 9000
        self.fuerza = min(self.fuerza, self.topeActual)





pepe = PajaroComun(100,20)
pepe.enojarse()
print("fuerza " +str(pepe.fuerza))
print("ira " + str(pepe.ira))