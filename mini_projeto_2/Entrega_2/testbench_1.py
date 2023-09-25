from ponto import Ponto
from reta import Reta
from quadrado import Quadrado
from circulo import Circulo
from triangulo import Triangulo
from retangulo import Retangulo

l = []
for c in range(0, 2):
    p = int(input('Digite um número que complete as coordenadas X e Y do ponto: '))
    l.append(p)
    
p1 = Ponto(l[0], l[1])
p1.Coordenadas()

l = []
for c in range(0, 4):
    p = int(input('Digite um número que complete as coordenadas A(Xa, Ya) e B(Xb, Yb): '))
    l.append(p)

r1 = Reta(l[0], l[1], l[2], l[3])
r1.Distancia()
r1.EquacaodaReta()

b1 = int(input('Qual a base do quadrado? '))
l1 = Quadrado(b1)
l1.Area()
l1.Perimetro()
l1.Diagonal()

c1 = Circulo(5, 0, 0)
c1.TesteDoRaio(3, 4)
c1.Area()

#O init está na respectiva ordem: ax, ay, bx, by, cx, cy. 
x = []
for c in range(0, 6):
    p = int(input('Digite um número que complete as coordenadas A(x, y), B(x, y) e C(x, y): '))
    x.append(p)

t1 = Triangulo(x[0], x[1], x[2], x[3], x[4], x[5])
t1.LadosDoTriangulo()
t1.Area()

b2 = int(input('Qual a base do Retângulo? '))
h2 = int(input('Qual a altura do Retângulo? '))
rg = Retangulo(b2, h2)
rg.Area()
rg.Diagonal()