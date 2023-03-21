class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        elif num < 0:
            sign = '-'
            num = abs(num)
        else:
            sign = ''
        res = ''
        while num:
            res = str(num % 7) + res
            num //= 7
        return sign + res