class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n <= 1:
            return False
        sum = 1
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                sum += i + n//i
        if int(n**0.5)**2 == n:
            sum -= int(n**0.5)
        return sum == n