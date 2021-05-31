from PajaroQueSeEnoja import PajaroQueSeEnoja

class Red(PajaroQueSeEnoja):
    def fuerza(self):
        return self._ira * 10 * self._CantidadDeVecesQueSeEnojo


juan = Red(10)
print(juan.fuerza())
juan.Enojarse()
print(juan._ira)
print(juan.fuerza())