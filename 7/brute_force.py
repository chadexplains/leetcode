class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        res = int(str(x)[::-1])
        if res > 2**31 - 1:
            return 0
        return sign * res
