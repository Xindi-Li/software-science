import re, traceback
from num import Num
from sample import Sample
from sym import Sym
from random import random
from random import seed


class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


@O.k
def testSample():
    seed(1)
    s = []
    for i in range(5, 11):
        s.append(Sample(2 ** i))
    for i in range(1, 10001):
        y = random()
        for t in s:
            t.sampleInc(y)
    for t in s:
        print(t.max, t.nth(0.5))
        assert 0.3 < t.nth(0.5) < 0.7


@O.k
def testNum():
    n = Num([4, 10, 15, 38, 54, 57, 62, 83, 100, 100, 174, 190, 215, 225,
             233, 250, 260, 270, 299, 300, 306, 333, 350, 375, 443, 475,
             525, 583, 780, 1000])
    print(n.mu, n.sd)
    assert n.mu == 270.3
    assert round(n.sd, 3) == 231.946


@O.k
def testSym():
    s = Sym(['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n'])
    assert abs(s.symEnt() - 0.9403)/s.symEnt()  < 0.01
    print(s.symEnt())


if __name__ == "__main__":
    O.report()
