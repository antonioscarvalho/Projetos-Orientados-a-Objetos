from math import sqrt
class Retangulo:
    def __init__(self, b, h):
        self.base = b
        self.altura = h
    
    def Area(self):
        Area = self.base * self.altura
        print(f'''Área: Base * Altura = {self.base} * {self.altura} = {Area}.
              ''')
        return
    
    def Diagonal(self):
        diagonal = sqrt(((self.base)**2)+(self.altura)**2)
        print(f'''Diagonal: raíz de {self.base}² + {self.altura}² = {diagonal:.2f}.
              ''')
        return
