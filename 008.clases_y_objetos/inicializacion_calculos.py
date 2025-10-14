# crear clase Rectangulo
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)

# crear objeto rectángulo
rectangulo = Rectangulo(5, 3)
print(rectangulo.area)
print(rectangulo.perimetro)