class Circulo:
    def __init__(self, centro, raio, PontoDeTeste):
        self.c = centro
        self.Raio = raio
        self.t1 = PontoDeTeste
    
    def TesteDoRaio(self):
        Dx = self.t1[0] - self.PontoDeTeste[0]
        Dy = self.t1[1] - self.PontoDeTeste[1]
        distancia = ((Dx)**2 + (Dy)**2)**(1/2)

        if distancia > self.Raio:
            return ("O ponto está fora do círculo")
        
        else:
            if distancia == self.Raio:
                return ("O ponto está em cima da circunferência do círculo")
            else:
                if distancia < self.Raio:
                    return ("O ponto está dentro do círculo")
    
    def Area(self):
        pi = 3.14159265
        area = pi * (self.Raio)**2
        print(f'Área: π x r² = {pi} x {self.Raio}² = {area}.')