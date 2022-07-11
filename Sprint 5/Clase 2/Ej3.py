import math


class Punto:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x != 0 and self.y == 0:
            return "Eje Y"
        elif self.x == 0 and self.y != 0:
            return "Eje X"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x > 0 and self.y > 0:
            return "Primer cuadrante"

    def vector(self,punto):
        return Punto(punto.x-self.x,punto.y-self.y)

    def distancia(self,punto):
        return math.sqrt((punto.x-self.x)**2+(punto.y-self.y)**2)


a = Punto(1,1)

b = Punto(2,2)

print(a.cuadrante())
print(a.vector(b))
print(a.distancia(b))
