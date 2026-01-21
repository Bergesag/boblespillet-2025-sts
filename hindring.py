""" Klassedefinisjon for Hindring"""
import random
from helt import Helt

tilfeldig = random.randint(20, 80)

class Hindring:
    """
    Det finnes hindringer i vannet som dukker opp. 
    Disse er kvadratiske og grå for enkelthets skyld.
    Kan være mangekanter hvis ønskelig.
    """
    def __init__(self, max_x=600, max_y=400):
        self.type = "hindring"
        self.farge = "grå"

        self.storrelse = tilfeldig

        self.x = random.randint(0, max_x - self.storrelse)
        self.y = random.randint(0, max_y - self.storrelse)



    def kollisjon(self,objekt2):
        """
        Hindringer har en annen algorite for å sjekke for kollisjon som ikke 
        benytter Pythagoras som gjelder for kollisjon mellom sirkler (boblene).
        Må se på overlapp av sirkelen og firkanten.
        """

        if (Helt.x + Helt.r < self.x):
            return False
        
        if (Helt.x - Helt.r > self.x + self.storrelse):
            return False
        
        if (Helt.y + Helt.r < self.y):
            return False
        
        if (Helt.y - Helt.r > self.y + self.storrelse):
            return False
        
        return True