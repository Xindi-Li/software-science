class Unsuper:

    def __init__(self, data):
        self.rows = data.rows
        self.enough = len(self.rows) ** 0.5
        for c in data.indeps:
            if data.nums[c]:
                self.ksort(c)
                self.most = self.stop(c)

    def band(self, c, lo, hi):
        if lo == 1:
            return f'..{self.rows[hi][c]}'
        elif hi

    def ksort(self, k):
        def cmp(a, b):
            x, y = a[k], b[k]
            if x == "?":
                return False
            elif y == "?":
                return True
            else:
                return x < y

        self.rows.sort(cmp=cmp)

    def stop(self, c):
        for i in range(len(self.rows) - 1, -1, -1):
            if self.rows[i][c] != "?":
                return i
        return 0
