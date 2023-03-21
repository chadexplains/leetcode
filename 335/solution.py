class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        if len(x) < 4:
            return False
        a, b, c, d, e = 0, x[0], x[1], x[2], x[3]
        for i in range(4, len(x)):
            if d >= b and b > 0 and (a >= c or (a >= c - e and f >= d - b)):
                return True
            f = e
            e = d
            d = c
            c = b
            b = x[i]
            a = x[i - 3]
        return False