class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def mostrar(self):
        return '* {}/{}.'.format(self.num, self.den)
