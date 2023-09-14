from math import sqrt, pi

class Circulo:
    def __init__(self, raio, centro_x, centro_y):
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.raio = raio

    def TesteDoRaio(self, ponto_x, ponto_y):
        distancia = sqrt((ponto_x - self.centro_x)**2 + (ponto_y - self.centro_y)**2)

        if distancia > self.raio:
            print("O ponto está fora do círculo.")
        elif distancia == self.raio:
            print("O ponto está em cima da circunferência do círculo.")
        else:
            print("O ponto está dentro do círculo.")

    def Area(self):
        area = pi * (self.raio**2)
        print(f"Área: π x r² = {pi} x {self.raio}² = {area}.")

        