import data
import math
from random import random
from test import O

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


def doms():
    n = 100
    da.name.append(">dom")
    for r1 in range(len(da.rows)):
        row1 = da.rows[r1]
        row1.append(0)
        for s in range(n):
            row2 = another(r1, da.rows)
            if dom(row1, row2):
                row1[-1] = row1[-1] + 1 / n
        row1[-1] = round(row1[-1], 2)
    return da.name, da.rows


def another(x, rows):
    y = max(0, math.floor(0.5 + random() * len(rows)) - 1)
    if x == y:
        return another(x, rows)
    else:
        return rows[y]


def weatherLong():
    global da
    da = data.rows("weatherLong.csv")
    res = doms()
    headers, rows = res[0], res[1]
    print("\t".join(headers))

    for row in rows:
        content = ""
        for cell in row:
            content += f'{cell}\t\t'
        print(content)


def auto():
    global da
    da = data.rows("auto.csv")
    res = doms()
    headers, rows = res[0], res[1]
    rows = sorted(rows, key=lambda i: i[-1])
    print("\t\t".join(headers))

    for i in range(11):
        content = ""
        row = rows[i]
        if i == 10:
            for cell in row:
                content += f'{"...":^15s}'
            print(content)
            break
        for cell in row:
            content += f'{str(cell):^15s}'
        print(content)

    for i in range(len(rows) - 10, len(rows)):
        content = ""
        row = rows[i]
        for cell in row:
            content += f'{str(cell):^15s}'
        print(content)


@O.k
def test1():
    weatherLong()


@O.k
def test2():
    auto()
