from math import sqrt
class Reta:
    def __init__(self, ax, bx, ay, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
    
    def EqdaReta(self):
        CoAng = (self.by - self.ay)/(self.bx - self.ax)
        CoLin = self.ay - CoAng * self.ax 
        EqdaReta = f"{CoAng} x X + {CoLin}"
        print(f'O coeficiente angular vale {CoAng}, o coeficiente linear vale {CoLin} e a equação da reta ficou caracterizada como {EqdaReta}.')
        return
    
    def Distancia(self):
        distanc = sqrt((self.bx - self.ax)**2 + (self.by - self.ay)**2)
        print(f'A distância da reta é de aproximadamente {distanc:.1f}.')
        return
