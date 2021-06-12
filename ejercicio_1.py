class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def mostrar(self):
        return '* {}/{}.'.format(self.num, self.den)


frac1 = Fraccion(9, 11)
frac2 = Fraccion(13, 14)
frac3 = Fraccion(10, 10)
print('Mostrar Fracciones: ')
print(frac1.mostrar())
print(frac2.mostrar())
print(frac3.mostrar())
