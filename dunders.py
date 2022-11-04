class Numero:

    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return f'Meu número: {self.numero}'

    def __repr__(self):
        return f'{self.numero}'

    def __neg__(self):
        self.numero = -self.numero
        return self.numero

    def __pos__(self):
        self.numero = +self.numero
        return self.numero

    def __add__(self, other):
        self.numero += other
        return self.numero
