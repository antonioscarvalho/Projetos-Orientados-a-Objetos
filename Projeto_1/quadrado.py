from math import sqrt
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def Area(self):
        area = (self.lado)**2
        return area
    
    def Diagonal(self):
        diagonal = sqrt(((self.lado)**2)+(self.lado)**2)
        return diagonal