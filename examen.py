
class Persona:
    def __init__(self,fuerza,resistencia):
        self.fuerza = fuerza
        self.resistencia = resistencia
      

    def aumentarFuerza(self,fuerzaAAumentar):
        self.fuerza += fuerzaAAumentar
        return None 

    def bajarFuerza(self,fuerzaABajar):
        self.fuerza -= fuerzaABajar 
        return None 

    def aumentarResistencia(self,resistenciaAAumentar):
        self.resistencia += resistenciaAAumentar 
        return None 

    def bajarResistencia(self,resistenciaABajar):
        self.resistencia -= resistenciaABajar 
        return None 

    def poder(self):
        return self.fuerza*self.resistencia

    def recibirDaño(self, daño):
        self.resistencia = max(0,self.resistencia-daño)
        return None 
    
    def estaFueraDeCombate(self):
        return self.resistencia==0

    def revivirSiEsPosible(self):
        if(self.estaFueraDeCombate()):
            self.resistencia +=2
        return None

    def tomar(self,pocion):
        pocion.aplicarEfectos(self)
        return None 
#  -------------------------------------------------------------------------------------------------------------------------

class Ejercito(Persona):
    def __init__(self,personas):
        self.soldados = personas

    def poderEjercito(self):
        poderEjercito = 0
        for soldado in self.soldados:
            poderEjercito += soldado.poder

        return poderEjercito

    def recibirDañoEjercito(self, daño):
        dañoDividido = daño/ max(self.soldados,10)
        for soldado in self.soldados:
            soldado.bajarResistencia(dañoDividido)
        return None
        

    
        

#  -------------------------------------------------------------------------------------------------------------------------


class Pocion:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes

    def aplicarEfectos(self, persona):
        for ingrediente in self.ingredientes:
            efecto = ingrediente.efecto()
            efecto(persona)
        return None

    
class DulceDeLeche:

    def efectoDulcedeleche(self,persona):
        persona.aumentarFuerza(10)
        persona.revivirSiEsPosible()
        
        return None



    def efecto(self):
        return self.efectoDulcedeleche 

class Grog:

    def efectoGrog(self,persona):
        persona.aumentarFuerza(pocion.ingredientes())
        
        return None

    def efecto(self):
        return self.efectoGrog 

#heredar el grog? !!!!

class GrogXD:

    def efectoGrogXD(self,persona):
        persona.aumentarFuerza(persona.fuerza*pocion.ingredientes())
        persona.aumentarResistencia(persona.resistencia*2)
        
        return None

    def efecto(self):
        return self.efectoGrogXD 



class PuñadoDeHongosSilvestres:
    def __init__(self,hongos):
        self.hongos = hongos


    def efectoPuñadoDeHongos(self,persona):
            persona.aumentarFuerza(self.hongos)
            if(persona.resistencia<5):
                persona.bajarResistencia(persona.resistencia/2)
            return None

    def efecto(self):
            return self.efectoPuñadoDeHongos 





#  ------------------------------------------------------------------------------------------------------------------------


# dulceDeLeche
# PuñadodeHongosSilvestres
# PuñadodeHongosSilvestres.cantidad
# pocion.obtenerEfecto(self)
# pocion.ingredientes
# pocion.cantidadDeIngredientes


fulano = Persona(10,10)
pocion = Pocion([DulceDeLeche(),PuñadoDeHongosSilvestres(5)])
print(fulano.fuerza)
print(fulano.resistencia)
fulano.tomar(pocion)
print(fulano.fuerza)
print(fulano.resistencia)
print(pocion.ingredientes)