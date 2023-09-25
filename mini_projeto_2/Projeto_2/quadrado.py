from math import sqrt
from retangulo import Retangulo
class Quadrado(Retangulo):
    
    def __init__(self, b):
        super().__init__(self, b)
        self.base = b
    
    def Area(self):
        area = self.base*self.base
        print(f'''Área: {self.base}² = {area}.
              ''')
        return
    
    def Diagonal(self):
        diagonal = sqrt(2)*self.base
        print(f'''Diagonal: raíz de 2 * lado = raíz de 2 * {self.base} = {diagonal:.2f}.
              ''')
        return
    
    def Perimetro(self):
        perimet = 4*(self.base)
        print(f'''Perímetro: 4 x {self.base} = {perimet}.
              ''')
        
