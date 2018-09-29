from vars import Vars
from num import Num
from test import O
import re
import data


class Unsuper:

    def __init__(self, data):
        self.rows = data.rows
        self.enough = len(self.rows) ** Vars.unsuper['enough']
        for c in data.indeps:
            if data.nums.get(c):
                self.ksort(c)
                self.most = self.stop(c)
                self.cuts(c, 0, self.most, "|.. ")
        for k, v in enumerate(data.name):
            if re.search(r'^\$', v):
                data.name[k] = re.sub(r'^\$', '', v)
        print('\t'.join(data.name))
        for row in data.rows:
            content = ""
            for cell in row:
                content += f'{cell}\t\t'
            print(content)

    def band(self, c, lo, hi):
        if lo == 0:
            return f'..{self.rows[hi][c]}'
        elif hi == self.most:
            return f'{self.rows[lo][c]}..'
        else:
            return f'{self.rows[lo][c]}..{self.rows[hi][c]}'

    def argmin(self, c, lo, hi):
        cut = None
        if hi - lo > self.enough:
            l, r = Num([]), Num([])
            for i in range(lo, hi + 1):
                r.numInc(int(self.rows[i][c]))
            best = r.sd
            for i in range(lo, hi + 1):
                x = int(self.rows[i][c])
                l.numInc(x)
                r.numDec(x)
                if l.n >= self.enough and r.n >= self.enough:
                    tmp = Num.numXpect(l, r) * Vars.unsuper['margin']
                    if tmp < best:
                        cut, best = i, tmp
        return cut

    def cuts(self, c, lo, hi, pre):
        txt = f'{pre}..{str(self.rows[lo][c])}..{str(self.rows[hi][c])}'
        cut = self.argmin(c, lo, hi)
        if cut:
            print(f'{txt}\n')
            self.cuts(c, lo, cut, f'{pre}|.. ')
            self.cuts(c, cut + 1, hi, f'{pre}|.. ')
        else:
            b = self.band(c, lo, hi)
            print(f'{txt} ({b})')
            for i in range(lo, hi + 1):
                self.rows[i][c] = b

    def ksort(self, k):
        self.rows.sort(key=lambda a: a[k])

    def stop(self, c):
        for i in range(len(self.rows) - 1, -1, -1):
            if self.rows[i][c] != "?":
                return i
        return 0


@O.k
def test():
    Unsuper(data.rows('weatherLong.csv'))
