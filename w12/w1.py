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



if __name__ == "__main__":
    O.report()
