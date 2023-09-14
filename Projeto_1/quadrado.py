from math import sqrt
class Quadrado:
    def __init__(self, b, h):
        self.lado1 = b
        self.lado2 = h
    
    def Area(self):
        area = (self.lado1)**2
        print(f'''Área: {self.lado1}² = {area}.
              ''')
        return
    
    def Diagonal(self):
        diagonal = sqrt(2)*self.lado1
        print(f'''Diagonal: raíz de 2 * lado = raíz de 2 * {self.lado1} = {diagonal:.2f}.
              ''')
        return
    
    def Perimetro(self):
        perimet = 4*(self.lado1)
        print(f'''Perímetro: 4 x {self.lado1} = {perimet}.
              ''')
