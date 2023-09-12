from reta import Reta

l = []
for c in range(0, 4):
    p = int(input('Digite um número que complete as coordenadas A(Xa, Ya) e B(Xb, Yb): '))
    l.append(p)

r1 = Reta(l[0], l[1], l[2], l[3])
r1.Distancia()
r1.EquacaodaReta()

from quadrado import Quadrado

lado = int(input('Qual o lado do quadrado? '))

l1 = Quadrado(lado)

l1.Area()
l1.Perimetro()
l1.Diagonal()

from circulo import Circulo

#O init está na respectiva ordem: centro, raio, ax, ay, ca, cb. Sendo esses últimos quatro os pontos de coordenadas para descobrir distância.

x = []
for c in range(0, 4):
    p = int(input('Digite um número que complete as coordenadas A(x, y) e C(a, b): '))
    x.append(p)

c1 = Circulo(1, 5, x[0], x[1], x[2], x[3])

c1.Area()
c1.TesteDoRaio()

from triangulo import Triangulo

#O init está na respectiva ordem: ax, ay, bx, by, cx, cy. 

x = []
for c in range(0, 6):
    p = int(input('Digite um número que complete as coordenadas A(x, y), B(x, y) e C(x, y): '))
    x.append(p)

t1 = Triangulo(x[0], x[1], x[2], x[3], x[4], x[5])

t1.LadosDoTriangulo()
t1.Area()