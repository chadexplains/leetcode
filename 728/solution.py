class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            for digit in str(num):
                if digit == '0' or num % int(digit) != 0:
                    return False
            return True
        res = []
        for num in range(left, right+1):
            if isSelfDividing(num):
                res.append(num)
        return res