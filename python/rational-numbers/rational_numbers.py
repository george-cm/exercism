from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
    
    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))