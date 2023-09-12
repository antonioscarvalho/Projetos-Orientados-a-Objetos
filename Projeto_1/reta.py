from math import sqrt
class Reta:
    def __init__(self, ax, bx, ay, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
    
    def EquacaodaReta(self):
        if (self.bx - self.ax) == 0:
            print('''
A equação da reta não pode ser feita, pois o Coeficiente Angular não pode ser calculado a partir de uma divisão por 0.
            ''')
        else:
            CoAng = (self.by - self.ay)/(self.bx - self.ax)
            CoLin = self.ay - CoAng * self.ax 
            EqdaReta = f"{CoAng} x X + {CoLin}"
            print(f'''
O coeficiente angular vale {CoAng:.2f}, o coeficiente linear vale {CoLin:.2f} e a equação da reta ficou caracterizada como {EqdaReta}.
            ''')
    
    def Distancia(self):
        distanc = sqrt((self.bx - self.ax)**2 + (self.by - self.ay)**2)
        print(f'''
A distância da reta é de aproximadamente {distanc:.1f}.
              ''')
        