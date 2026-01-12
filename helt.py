"""Klassedefinisjon for Helt"""
from boble import Boble

class Helt(Boble):
    def __init__(self, r, x, y):
        super().__init__(r, x, y)
        self.type = "helt"
        self.poeng = 0
    
    def sett_ny_fart(self,dx,dy):
        pass

    def kollisjon(self, objekt2):
        """
        Hvis helten treffer en annen boble skal den spise den andre hvis mindre.
        Ellers dør helten.
        """
        pass
    def tegnBoble(self, xpos,ypos,R=50):
        canvas.create_oval(xpos-R,ypos-R,xpos+R,ypos+R,fill="#ff9944", tags="boble")