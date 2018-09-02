import re, traceback


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


DATA1 = """
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 = """
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""


def lines(s):
    "Return contents, one line at a time."
    return [i.strip() for i in s.split('\n')]


def rows(src):
    """Kill bad characters. If line ends in ','
     then join to next. Skip blank lines."""
    res = []
    pre = ""
    for line in src:
        if line == '':
            continue
        match = re.match(r'(.*)#.*', line)
        if match:
            line = match.group(1).strip()
        if re.search(r',$', line):
            pre += line
        else:
            if pre != "":
                pre += line
                res.append(pre)
                pre = ""
            else:
                res.append(line)
    return res


def cols(src):
    """ If a column name on row1 contains '?',
    then skip over that column."""
    res = []
    ignore = set()
    for i, item in enumerate(src[0].split(',')):
        if re.search(r'^\?', item):
            ignore.add(i)
    if len(ignore) == 0:
        res = src
    else:
        for item in src:
            lis = item.split(',')
            for index in ignore:
                del lis[index]
            res.append(','.join(lis))
    return res


def prep(src):
    """ If a column name on row1 contains '$',
    coerce strings in that column to a float."""
    res = []
    convert = set()
    res.append(src[0])
    for i, item in enumerate(src[0].split(',')):
        if re.search(r'^\$', item):
            convert.add(i)
    if len(convert) == 0:
        res = src
    else:
        for item in src[1:]:
            lis = item.split(',')
            for index in convert:
                lis[index] = str(float(lis[index]))
            res.append(','.join(lis))
    return res


def ok0(s):
    for row in prep(cols(rows(lines(s)))):
        print(row)


@O.k
def ok1(): ok0(DATA1)


@O.k
def ok2(): ok0(DATA2)
