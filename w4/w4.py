from sym import Sym
from num import Num
from test import O
import sys
import re


class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self._class = None
        self.rows = []
        self.name = []
        self._use = []
        self.indeps = []

    def indep(self, c):
        return c not in self.w and self._class != c

    def dep(self, c):
        return not self.indep(c)

    def header(self, cells):
        for i, v in enumerate(cells):
            if not re.match(r'^\?', v):
                c = len(self._use)
                self._use.append(i)
                self.name.append(v)
                if re.search('[<>$]', v):
                    self.nums[c] = Num([])
                else:
                    self.syms[c] = Sym([])
                if re.search('<', v):
                    self.w[c] = -1
                elif re.search('>', v):
                    self.w[c] = 1
                elif re.search('!', v):
                    self._class = c
                else:
                    self.indeps.append(c)

    def row(self, cells):
        r = len(self.rows)
        self.rows.append([])
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if x != '?':
                if self.nums.get(c) is not None:
                    self.nums[c].numInc(float(x))
                else:
                    self.syms[c].symInc(x)
            self.rows[r].append(x)


def rows1(src):
    data = Data()
    first = True
    for line in src:
        line = re.sub('[\t\r\n]*|#.*', "", line)
        cells = [i.strip() for i in line.split(',')]
        if len(cells) > 0:
            if first:
                data.header(cells)
            else:
                data.row(cells)
            first = False
    print("\t\t\tn\tmode\tfrequency")
    for k, v in data.syms.items():
        print(f'{k+1}\t{data.name[k]}\t{v.n}\t{v.mode}\t{v.most}')
    print('\n')
    print('\t\t\tn\tmu\tsd')
    for k, v in data.nums.items():
        print(f'{k+1}\t{data.name[k]}\t{v.n}\t{v.mu:.2f}\t{v.sd:.2f}')


def lines(src=None):
    if src == None:
        for line in sys.stdin:
            yield line
    elif src[-3:] in ["csv", ".dat"]:
        with open(src) as fs:
            for line in fs:
                yield line
    else:
        for line in src.splitlines():
            yield line


def rows(s):
    rows1(lines(s))


@O.k
def test():
    print("\nweather.csv\n")
    rows("weather.csv")
    print("\nweatherLong.csv\n")
    rows("weatherLong.csv")
    print("\nauto.csv\n")
    rows("auto.csv")