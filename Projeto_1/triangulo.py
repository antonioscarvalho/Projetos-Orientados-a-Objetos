from math import sqrt
class Triangulo:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def LadosDoTriangulo(self):
        lado1 = sqrt((self.ax - self.bx)**2 + (self.ay - self.by)**2)
        lado2 = sqrt((self.bx - self.cx)**2 + (self.by - self.cy)**2)
        lado3 = sqrt((self.cx - self.ax)**2 + (self.cy - self.ay)**2)
        print(f'''
Distancia do primeiro ponto até o segundo = {lado1}
Distancia do segundo ponto até o terceiro = {lado2}
Distancia do terceiro ponto até o primeiro = {lado3}''')

    def Area(self):
        lado1 = sqrt((self.ax - self.bx)**2 + (self.ay - self.by)**2)
        lado2 = sqrt((self.bx - self.cx)**2 + (self.by - self.cy)**2)
        lado3 = sqrt((self.cx - self.ax)**2 + (self.cy - self.ay)**2)
        l = [lado1, lado2, lado3]
        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            print('''
Elas conseguem formar um triâgulo.
                  ''')

        if lado1 == lado2 == lado3:
            print('''
E esse triângulo é equilatero.
                  ''')
            area = ((lado1)**2)*(sqrt(3))/4
            print(f'''
Área do triângulo equilatero: {area}
''')

        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('''
E esse triângulo é isóceles.
                  ''')
            maior = []
            maior.append(max(l))
            h = sqrt(lado1**2 + (maior[0]/2)**2)
            area = (maior[0] * h)/2
            print(f'''
Área do triângulo isóceles: {area}
''')

        elif lado1 != lado2 != lado3:
            print('''
E esse triângulo é escaleno.
                  ''')
            #Fórmula de Heron para calcular a área do triângulo escaleno.
            semiperimetro = (lado1 + lado2 + lado3)/2
            area = sqrt(semiperimetro*(semiperimetro - lado1)*(semiperimetro-lado2)*(semiperimetro-lado3))
            print(f'''
Área do triângulo escaleno: {area}
                  ''')

        else:
            print('''
Não conseguem formar um triângulo.
                  ''')
