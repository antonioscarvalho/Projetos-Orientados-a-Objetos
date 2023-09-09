from reta import Reta

l = []
for c in range(0, 4):
    p = int(input('Digite um número que complete as coordenadas A(Xa, Ya) e B(Xb, Yb): '))
    l.append(p)

r1 = Reta(l[0], l[1], l[2], l[3])

r1.Distancia()
print(f'''
{r1}
''')
r1.EquacaodaReta()
print(f'''
{r1}
''')

from quadrado import Quadrado

lado = int(input('Qual o lado do quadrado? '))

l1 = Quadrado(lado)

l1.Area()
print(f'''
{l1}
''')
l1.Perimetro()
print(f'''
{l1}
''')
l1.Diagonal()
print(f'''
{l1}
''')

from circulo import Circulo

#O init está na respectiva ordem: centro, raio, ax, ay, ca, cb. Sendo esses últimos quatro os pontos de coordenadas para descobrir distância.

x = []
for c in range(0, 4):
    p = int(input('Digite um número que complete as coordenadas A(x, y) e C(a, b): '))
    x.append(p)

c1 = Circulo(1, 5, x[0], x[1], x[2], x[3])

c1.Area()
print(f'''{c1}
''')

c1.TesteDoRaio()
print(f'''
{c1}
''')
