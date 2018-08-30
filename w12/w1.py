import re, traceback
from collections import defaultdict
from collections import Counter
import random
from functools import partial
from functools import reduce


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
def testing_page5():
    """whitespace formatting"""
    tup = (1, 2, 3
           , 4)
    assert sum(tup) == 10


@O.k
def testing_page6():
    """re module"""
    assert "abc" == re.sub("^.", 'a', 'bbc')


@O.k
def testing_page7():
    """Arithmetic"""
    assert 5 / 2 == 2.5
    assert 5 // 2 == 2


@O.k
def testing_page8():
    """Functions"""

    def double(x):
        return x * 2

    def applytwo(f):
        return f(2)

    assert applytwo(double) == 4

    assert applytwo(lambda x: x + 10) == 12

    def add(a=1, b=1):
        return a + b

    assert add() == 2


@O.k
def testing_page9():
    """Strings"""
    assert len("\n") == 1
    assert len(r"\n") == 2


@O.k
def testing_page10():
    """Exceptions"""
    try:
        print(0 / 0)
    except ZeroDivisionError:
        assert True


@O.k
def testing_page11():
    """Lists"""
    l = [1, 2, 3]
    assert 1 in l
    l.extend([4, 5, 6])
    assert 4 in l


@O.k
def testing_page12():
    """unpack Lists"""
    x, y = [3, 4]
    assert y == 4


@O.k
def testing_page13():
    """tuples"""
    tup = (1, 3)
    try:
        tup[1] = 0
    except:
        assert True


@O.k
def testing_page14():
    """dictionaries"""
    dic = {"abc": 1}
    assert "abc" in dic


@O.k
def testing_page15():
    """defaultdict"""
    word_count = defaultdict(int)
    for word in ['you', 'I', 'He', 'you', 'you']:
        word_count[word] += 1
    assert word_count['you'] == 3


@O.k
def testing_page16():
    """counter"""
    word_count = Counter(['you', 'I', 'He', 'you', 'you'])
    assert word_count['you'] == 3


@O.k
def testing_page17():
    """sets"""
    s = set()
    s.add(1)
    s.add(1)
    s.add(2)
    assert len(s) == 2


@O.k
def testing_page18():
    """control flow"""
    num = 0
    while num < 10:
        num += 1
    assert num == 10


@O.k
def testing_page19():
    """truthiness"""
    assert bool(1 < 2) == True
    assert 0 == False


@O.k
def testing_page20():
    """all fucntion"""
    assert any([bool(1 < 2), False, 0]) == True
    assert all([0.0, ""]) == False


@O.k
def testing_page22():
    """sorting"""
    x = [1, 2, 3]
    x.sort(reverse=True)
    assert x[0] == 3


@O.k
def testing_page23():
    """list comprehensions"""
    inc = [(x, y)
           for x in range(10)
           for y in range(x + 1, 10)]
    assert inc[0][1] == 1


@O.k
def testing_page24():
    """generators and iterators. In python3, dict.items now does the thing dict.iteritems did in python 2.x """
    dic = {1: 1, 2: 2, 3: 3, 4: 4}
    for k, v in dic.items():
        assert k == v


@O.k
def testing_page25():
    """randomness"""
    lis = [1, 2, 3, 3, 4, 5, 65]
    assert random.choice(lis) != random.choice(lis)


@O.k
def testing_page26():
    """regular expressions"""
    assert re.match(r'.*cat.*', "asbdcat@@@") is not None


@O.k
def testing_page27():
    """oo programming"""

    class Calculate:
        def times2(self, x):
            return 2 * x

    cal = Calculate()
    assert cal.times2(2) == 4


@O.k
def testing_page28():
    """functional tools"""

    def multiply(x, y):
        return x * y

    times3 = partial(multiply, 3)
    assert times3(5) == 15


@O.k
def testing_page29():
    """reduce"""

    def multiply(x, y):
        return x * y

    res = reduce(multiply, [1, 2, 3, 4])
    assert res == 24


@O.k
def testing_page30():
    """enumerate"""

    lis = [0, 1, 2, 3, 4, 5]
    for index, val in enumerate(lis):
        assert index == val


@O.k
def testing_page31():
    """zip and argument unpacking"""

    a = list(zip([1, 2, 3], [4, 5, 6]))
    assert a[1][1] == 5

    multi = lambda x, y: x * y
    assert multi(*[2, 3]) == 6


@O.k
def testing_page32():
    """args and kwargs"""

    def lenargs(*args, **kwargs):
        return len(args), len(kwargs)

    assert lenargs(1, 2, 3, 4, 5, 6, k1='1', k2='2', k3='3')[0] == 6
    assert lenargs(1, 2, 3, 4, 5, 6, k1='1', k2='2', k3='3')[1] == 3


@O.k
def testing_page33():
    """higher-order functions"""

    def multiply(x, y):
        return x * y

    def double(f):
        def g(*args, **kwargs):
            return 2 * f(*args, **kwargs)

        return g

    v = double(multiply)
    assert v(2, 3) == 12


if __name__ == "__main__":
    O.report()
