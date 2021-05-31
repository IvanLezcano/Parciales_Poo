from PajaroQueSeEnoja import PajaroQueSeEnoja

class Terance(PajaroQueSeEnoja):
    def __init__(self,ira,multiplicador):
        super().__init__(ira)
        self._multiplicador = multiplicador

    def fuerza(self):

        return self._ira * self._multiplicador * self._CantidadDeVecesQueSeEnojo


elLoco = Terance(30,3)
# elLoco.Enojarse()
# elLoco.fuerza()
