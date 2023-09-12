from math import sqrt
class Circulo:
    def __init__(self, centro, Raio, ax, ay, ca, cb):
        self.c = centro
        self.Raio = Raio
        self.ax = ax
        self.ay = ay
        self.ca = ca
        self.cb = cb
    
    def TesteDoRaio(self):
        distancia = sqrt((self.ax - self.ay)**2 + (self.ca - self.cb)**2)
        print(f'''
Distância: raíz de {self.ax - self.ay}² + {self.ca - self.cb}² = {distancia}.
''')

        if distancia > self.Raio:
            print('''
O ponto está fora do círculo.
                  ''')
        else:
            if distancia == self.Raio:
                print('''
O ponto está em cima da circunferência do círculo.
                      ''')
            else:
                if distancia < self.Raio:
                    print('''
O ponto está dentro do círculo.
                          ''')

    def Area(self):
        pi = 3.14159265
        area = pi * (self.Raio)**2
        print(f'''
Área: π x r² = {pi} x {self.Raio}² = {area}.
              ''')
        