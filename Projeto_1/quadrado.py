from math import sqrt
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def Area(self):
        area = (self.lado)**2
        print(f'''Área: {self.lado}² = {area}.
              ''')
        return
    
    def Diagonal(self):
        diagonal = sqrt(((self.lado)**2)+(self.lado)**2)
        print(f'''Diagonal: raíz de {self.lado}² + {self.lado}² = {diagonal:.2f}.
              ''')
        return
    
    def Perimetro(self):
        perimet = 4*(self.lado)
        print(f'''Perímetro: 4 x {self.lado} = {perimet}.
              ''')
