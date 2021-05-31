from Pajaro import *

class PajaroComun(Pajaro):
    def __init__(self, fuerza, ira):
        super().__init__(fuerza, ira)
        self._fuerza = self._ira*2



