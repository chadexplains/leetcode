class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n_str = str(n)
            n = sum(int(digit)**2 for digit in n_str)
            if n in seen:
                return False
            seen.add(n)
        return True