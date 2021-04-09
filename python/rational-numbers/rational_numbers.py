from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        r1 = self._simplify(self.numer, self.denom)
        r2 = self._simplify(other.numer, other.denom)
        return r1.numer == r2.numer and r1.denom == r2.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom
        return self._simplify(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom
        return self._simplify(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return self._simplify(numer, denom)

    def __truediv__(self, other):
        denom = self.denom * other.numer
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        numer = self.numer * other.denom
        return self._simplify(numer, denom)
        

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return self._simplify(self.numer ** power, self.denom ** power)
        else:
            return self._simplify(self.denom ** abs(power), self.numer ** abs(power))

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)
    
    def _simplify(self, numer, denom):
        gcd = self._gcd(numer, denom)
        numer = numer/gcd
        denom = denom/gcd
        if denom < 0:
            denom *= -1
            numer *= -1
        return Rational(numer, denom)
    
    def _gcd(self, a, b):
        # binary GCD algorithm from https://en.wikipedia.org/wiki/Binary_GCD_algorithm
        # The algorithm reduces the problem of finding the GCD of two nonnegative numbers v and u by repeatedly applying these identities:
        # gcd(0, v) = v, because everything divides zero, and v is the largest number that divides v. Similarly, gcd(u, 0) = u.
        # gcd(2u, 2v) = 2·gcd(u, v)
        # gcd(2u, v) = gcd(u, v), if v is odd (2 is not a common divisor). Similarly, gcd(u, 2v) = gcd(u, v) if u is odd.
        # gcd(u, v) = gcd(|u − v|, min(u, v)), if u and v are both odd.
        
        u = abs(a)
        v = abs(b)

        # base cases
        # gcd(n, n) = n
        if u == v:
            return u
        
        # identity 1: gcd(0, n) = gcd(n, 0) = n
        if u == 0:
            return v
        if v == 0:
            return u
        
        if u % 2 == 0: # u is even
            if v % 2 == 1: # v is odd
                return self._gcd(u/2, v) # identity 3
            else: # both u and v are even
                return 2 * self._gcd(u/2, v/2) # identity 2
        else: # u is odd
            if v % 2 == 0: # v is even
                return self._gcd(u, v/2) # identity 3

            # identities 4 and 3 (u and v are odd, so u-v and v-u are known to be even)
            if (u > v):
                return self._gcd((u-v)/2, v)
            else:
                return self._gcd((v-u)/2, u)