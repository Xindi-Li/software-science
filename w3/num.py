from sample import Sample
from vars import Vars
from test import O


class Num:
    def __init__(self, l, f=lambda x: x):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = Vars().lo
        self.hi = Vars().hi
        self.some = Sample()
        self.w = 1
        for i in l:
            self.numInc(f(i))

    def numInc(self, x):
        if x == "?":
            return x
        self.n += 1
        self.some.sampleInc(x)
        d = x - self.mu
        self.mu = self.mu + d / self.n
        self.m2 = self.m2 + d * (x - self.mu)
        if x > self.hi:
            self.hi = x
        if x < self.hi:
            self.lo = x
        if self.n >= 2:
            self.sd = (self.m2 / (self.n - 1 + 10 ** -32)) ** 0.5
        return x

    def numDec(self, x):
        if x == "?":
            return x
        if self.n == 1:
            return x
        self.n -= 1
        d = x - self.mu
        self.mu = self.mu - d / self.n
        self.m2 = self.m2 - d * (x - self.mu)
        if self.n >= 2:
            self.sd = (self.m2 / (self.n - 1 + 10 ** -32)) ** 0.5
        return x

    def numNorm(self, x):
        return 0.5 if x == "?" else (x - self.lo) / (self.hi - self.lo + 10 ** -32)

    def numXpect(self, i, j):
        n = i.n + j.n + 0.001
        return i.n / n * i.sd + j.n / n * j.sd


@O.k
def test():
    n = Num([4, 10, 15, 38, 54, 57, 62, 83, 100, 100, 174, 190, 215, 225,
             233, 250, 260, 270, 299, 300, 306, 333, 350, 375, 443, 475,
             525, 583, 780, 1000])
    print(n.mu, n.sd)
    assert n.mu == 270.3
    assert round(n.sd, 3) == 231.946
