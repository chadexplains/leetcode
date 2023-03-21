class Solution:
    def isThree(self, n: int) -> bool:
        if int(n**0.5)**2 != n:
            return False
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                return False
        return int(n**0.5) > 1