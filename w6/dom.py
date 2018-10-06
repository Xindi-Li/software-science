import data
import math
from vars import Vars
from random import random

da = None


def dom(row1, row2):
    s1, s2 = 0, 0
    n = len(da.w)
    for c, w in da.w.items():
        a0 = float(row1[c])
        b0 = float(row2[c])
        a = data.numNorm(da.nums[c], a0)
        b = data.numNorm(da.nums[c], b0)
        s1 = s1 - 10 ** (w * (a - b) / n)
        s2 = s2 - 10 ** (w * (b - a) / n)
    return s1 / n < s2 / n


def doms(src):
    global da
    da = data.rows(src)
    n = Vars.dom['samples']
    da.name.append(">dom")
    for r1 in range(len(da.rows)):
        row1 = da.rows[r1]
        row1.append(0)
        for s in range(n):
            row2 = another(r1, da.rows)
            if dom(row1, row2):
                row1[-1] = row1[-1] + 1 / n
        row1[-1] = round(row1[-1], 2)
    return da


def another(x, rows):
    y = max(0, math.floor(0.5 + random() * len(rows)) - 1)
    if x == y:
        return another(x, rows)
    else:
        return rows[y]
