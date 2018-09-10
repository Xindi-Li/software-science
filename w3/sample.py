from vars import Vars
from random import random
from random import seed
import math

class Sample:

    def __init__(self, max=Vars.max):
        self.max = max
        self.n = 0
        self.sorted = False
        self.some = []

    def sampleInc(self, x):
        self.n += 1
        now = len(self.some)
        if now < self.max:
            self.sorted = False
            self.some.append(x)
        elif random() < now / self.n:
            self.sorted = False
            self.some[math.floor(0.5 + random() * now) - 1] = x
        return x

    def sampleSorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some

    def nth(self, n):
        s = self.sampleSorted()
        return s[min(len(s) - 1, max(1, math.floor(0.5 + len(s) * n)))]

    def nths(self, ns=(0.1, 0.3, 0.5, 0.7, 0.9)):
        out = []
        for n in ns:
            out.append(self.nth(n))
        return out



