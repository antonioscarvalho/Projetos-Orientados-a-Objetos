from math import sqrt
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def Area(self):
        area = (self.lado)**2
        print(f'A área é {area:.2f}.')
        return
    
    def Diagonal(self):
        diagonal = sqrt(((self.lado)**2)+(self.lado)**2)
        print(f'A diagonal é {diagonal:.2f}.')
        return
