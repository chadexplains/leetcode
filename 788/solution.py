class Solution:
    def rotatedDigits(self, N: int) -> int:
        def is_good(num):
            s = str(num)
            if '3' in s or '4' in s or '7' in s:
                return False
            if '2' in s or '5' in s or '6' in s or '9' in s:
                return True
            return False
        count = 0
        for i in range(1, N+1):
            if is_good(i):
                count += 1
        return count