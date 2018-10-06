from vars import Vars
from num import Num
from test import O
import re
import math
import dom


class Super:

    def __init__(self, data):
        self.name = data.name.copy()
        self.sd_split = {}
        self.rows = data.rows
        self.enough = len(data.rows) ** Vars.unsuper['enough']
        self.goal = len(data.rows[1]) - 1
        for k, v in enumerate(data.name):
            if re.search(r'^\$', v):
                data.name[k] = re.sub(r'^\$', '', v)

        for c in data.indeps:
            if data.nums.get(c):
                self.ksort(c)
                self.most = self.stop(c)
                print(f'\n-- {self.name[c]} ----------')
                self.cuts(c, 0, self.most, "|.. ")

        print('\t'.join(data.name))
        for row in data.rows:
            content = ""
            for cell in row:
                content += f'{cell}\t\t'
            print(content)
        print('\n')
        self.splitter()

    def band(self, c, lo, hi):
        if lo == 0:
            return f'..{self.rows[hi][c]}'
        elif hi == self.most:
            return f'{self.rows[lo][c]}..'
        else:
            return f'{self.rows[lo][c]}..{self.rows[hi][c]}'

    def argmin(self, c, lo, hi):
        cut = None
        xl, xr = Num([]), Num([])
        yl, yr = Num([]), Num([])
        for i in range(lo, hi + 1):
            xr.numInc(float(self.rows[i][c]))
            yr.numInc(float(self.rows[i][self.goal]))
        bestx = xr.sd
        besty = yr.sd
        mu = yr.mu
        sd = yr.sd
        if hi - lo > self.enough * 2:
            for i in range(lo, hi + 1):
                x = float(self.rows[i][c])
                y = float(self.rows[i][self.goal])
                xl.numInc(x)
                xr.numDec(x)
                yl.numInc(y)
                yr.numDec(y)
                if xl.n >= self.enough and xr.n >= self.enough:
                    tmpx = Num.numXpect(xl, xr) * Vars.unsuper['margin']
                    tmpy = Num.numXpect(yl, yr) * Vars.unsuper['margin']
                    if type(tmpx) == "complex":
                        continue
                    if tmpx < bestx and tmpy < besty:
                        cut, bestx, besty = i, tmpx, tmpy

        return cut, mu, sd

    def cuts(self, c, lo, hi, pre):
        txt = f'{pre}..{str(self.rows[lo][c])}..{str(self.rows[hi][c])}'
        cut, mu, sd = self.argmin(c, lo, hi)
        if cut:
            print(txt)
            self.cuts(c, lo, cut, f'{pre}|.. ')
            self.cuts(c, cut + 1, hi, f'{pre}|.. ')
        else:
            b = self.band(c, lo, hi)
            if self.sd_split.get(self.name[c]) is None:
                self.sd_split[self.name[c]] = {}
            self.sd_split[self.name[c]][math.floor(100 * mu)] = sd
            print(f'{txt} = {math.floor(100*mu)}')
            for i in range(lo, hi + 1):
                self.rows[i][c] = b

    def ksort(self, k):
        self.rows.sort(key=lambda a: math.inf if a[k] == '?' else float(a[k]))

    def stop(self, c):
        for i in range(len(self.rows) - 1, -1, -1):
            if self.rows[i][c] != "?":
                return i
        return 0

    def splitter(self):
        min_sd = math.inf
        for name in self.sd_split.keys():
            vs = self.sd_split[name]
            n = sum(vs.keys())
            e_sd = 0
            for k, v in vs.items():
                e_sd += k / n * v
            print(f'expected sd when split on {name} = {e_sd}')
            if e_sd < min_sd:
                min_sd = e_sd
                split = name
        print(f'Splitter is {split}')


@O.k
def testWeather():
    Super(dom.doms("weatherLong.csv"))


@O.k
def testAuto():
    Super(dom.doms("auto.csv"))
