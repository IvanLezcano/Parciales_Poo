from Pajaro import Pajaro

class PajaroQueSeEnoja(Pajaro):
    def __init__(self,ira):
        super().__init__(ira)
        self._CantidadDeVecesQueSeEnojo = 0

    def Enojarse(self):
        self._ira = self._ira * 2
        self._CantidadDeVecesQueSeEnojo += 1
        return None
    

pepe = PajaroQueSeEnoja(10)

print(pepe.fuerza())