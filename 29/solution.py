class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > -2**31:
                return -dividend
            else:
                return 2**31 - 1
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            res += multiple
        if sign == -1:
            res = -res
        if res > 2**31 - 1:
            return 2**31 - 1
        return res