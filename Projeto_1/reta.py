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
        return EqdaReta
    
    def Distancia(self):
        distanc = sqrt((self.bx - self.ax)**2 + (self.by - self.ay)**2)
        return distanc
